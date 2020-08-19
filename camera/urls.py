from django.urls import path

from .views import index, StudentView,  StudentList, StudentDetail


urlpatterns = [
    path('', index, name='index'),
    # path('student/<int:pk>', StudentView.as_view(), name='student'),
    path('student/', StudentList.as_view(), name='category-list'),
    path('student/<int:pk>', StudentDetail.as_view(), name='category-detail'),



]