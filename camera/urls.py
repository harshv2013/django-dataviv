from django.urls import path

from .views import index, \
    UserCreate, LoginView, UserList, UserDetail, \
    OrganizationListCreate, \
    OrganizationRetriveUpdateDestroy, EmployeeListCreate, \
    EmployeeRetriveUpdateDestroy, StoreListCreate, \
    StoreRetriveUpdateDestroy

urlpatterns = [
    path('', index, name='index'),
    path('organization/', OrganizationListCreate.as_view(), name='category-list'),
    path('organization/<int:pk>', OrganizationRetriveUpdateDestroy.as_view(), name='category-list'),
    # path('employee/', EmployeeList.as_view(), name='employee-list'),
    # path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee-list'),
    path('employee/', EmployeeListCreate.as_view(), name='employee-list'),
    path('employee/<int:pk>', EmployeeRetriveUpdateDestroy.as_view(), name='employee-detail'),
    path('store/', StoreListCreate.as_view(), name='store-list'),
    path('store/<int:pk>', StoreRetriveUpdateDestroy.as_view(), name='store-detail'),
    path("usercreate/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),


]