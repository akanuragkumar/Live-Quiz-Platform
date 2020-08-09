from django.views.generic import RedirectView
from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('joinquiz/', views.joinQuiz, name='joinQuiz'),
    path('createaccount/', views.createAccount, name='createAccount'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/createQuiz/', views.createQuiz, name='createQuiz'),
    path('accounts/editQuiz/quiz-<int:quizID>/', views.editQuiz, name = 'editQuiz'),
    path('accounts/editQuestion/quiz-<int:quizID>/question-<int:questionID>/', views.editQuestion, name = 'editQuestion'),
    path('accounts/editAnswer/quiz-<int:quizID>/question-<int:questionID>/answer-<int:answerID>/', views.editAnswer, name = 'editAnswer'),
    path('startquiz/quiz-<int:quizID>/', views.startQuiz, name='startQuiz'),
    path('joinquiz/<room_name>/', views.roomJoin, name="roomJoin"),
    path('hostquiz/<room_name>/', views.teacherView , name='roomMain'),
]