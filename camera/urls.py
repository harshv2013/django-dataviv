from django.urls import path

from .views import index, StudentView,  StudentList, StudentDetail,\
    EmployeeList, UserCreate, LoginView, UserList, UserDetail


urlpatterns = [
    path('', index, name='index'),
    # path('student/<int:pk>', StudentView.as_view(), name='student'),
    path('student/', StudentList.as_view(), name='category-list'),
    path('student/<int:pk>', StudentDetail.as_view(), name='category-detail'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path("usercreate/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),


]