from django.contrib import admin
from django.urls import path
from .views import StudentAddApi ,StudentAllApi,StudentUpdateApi,StudentDeleteApi,StudentGetApi

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('students/',StudentAllApi.as_view()),
    path('add/',StudentAddApi.as_view()),
    path('update/<int:id>',StudentUpdateApi.as_view()),
    path('delete/<int:id>x',StudentDeleteApi.as_view()),
    path('students/<int:id>',StudentGetApi.as_view())
    
    # path('/all',StudentApi.as_view())
]