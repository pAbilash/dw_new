from django.shortcuts import render,HttpResponse

# Create your views here.
from token_app.models import Test
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from token_app.serializers import TestSerializer
from fuzzywuzzy import fuzz
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
class TestApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        if request.method == 'GET':
            que_obj = Test.objects.filter(question_id=pk)
            que_ser_obj = TestSerializer(que_obj, many=True)
            return Response(que_ser_obj.data,status=status.HTTP_200_OK)
        else:
            return Response(que_ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)

class TestAnswerApiView(APIView):
    def post(self, request,*args,**kwargs):
        if request.method == 'POST':
            id = request.POST['question_id']
            answer = request.POST['user_answer']
            que_obj = Test.objects.get(question_id=id)
            user_ans = que_obj.answer
            sentences = word_tokenize(user_ans)
            stop_words = set(stopwords.words('english'))
            words = [w for w in sentences if not w in stop_words]
            print(words)
            que_obj.user_answer = answer
            answer_percentage = fuzz.token_sort_ratio(answer, words)
            que_obj.percentage = answer_percentage
            que_obj.save()
            return Response(fuzz.token_sort_ratio(answer, words),status=status.HTTP_200_OK)
        else:
            return Response(fuzz.token_sort_ratio(answer, words), status=status.HTTP_400_BAD_REQUEST)

class TotalMarks(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            objects = []
            all_objects = Test.objects.all()
            for i in all_objects:
                objects.append(i.percentage)
            print(objects)
            avg = sum(objects)/len(objects)

            return Response(avg,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)