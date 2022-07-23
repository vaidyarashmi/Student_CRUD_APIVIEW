from django.urls import path,include
from testapp import views
urlpatterns = [
    path('api/', views.StudentCRUDCBV.as_view()),
]