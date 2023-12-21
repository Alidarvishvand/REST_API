
from django.urls import path
from . import views

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

router = routers.SimpleRouter()
router.register('user',views.UserViewSet)
urlpatterns += router.urls


# {
# 	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjkxNTM5MCwiaWF0IjoxNzAyODI4OTkwLCJqdGkiOiIyNWFjYmYzMWExMGU0YTljOWMwYTVkYjc3YjFjNTI2ZSIsInVzZXJfaWQiOjZ9.ShxYhYzJoDsFovFE14fRLkLO5tIUBU_l9--uI-Mg-Kc",
# 	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyODI5MjkwLCJpYXQiOjE3MDI4Mjg5OTAsImp0aSI6ImUzNDk4M2FlYmVjZjQ5OTJiMmE0YzhiOTg4MmRlYTJlIiwidXNlcl9pZCI6Nn0.lFXS_bVooCy8owpFM63paVK0OMT_EC6jpPH7NXy9Aro"
# }