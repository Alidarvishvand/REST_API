
from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.HOME.as_view(),name='home'),
    path('questions/',views.Questionlistview.as_view()),
    path('questions/creat/',views.questioncreatview.as_view()),
    path('question/update/<int:pk>/',views.questionupdateview.as_view()),
    path('question/delete/<int:pk>/',views.questiondeletview.as_view())

]

 