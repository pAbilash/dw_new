from django.urls import path, include
from token_app.views import TestApiView,TestAnswerApiView,TotalMarks
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings
   

urlpatterns = [
    path('question/<int:pk>', TestApiView.as_view()),
    path('answer', TestAnswerApiView.as_view()),
    path('marks', TotalMarks.as_view()),

] 

if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)