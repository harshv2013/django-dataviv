from django.urls import path, re_path

from django.conf.urls import url

from .views import index, \
    UserCreate, LoginView, UserList, UserDetail, \
    OrganizationListCreate, \
    OrganizationRetriveUpdateDestroy, EmployeeListCreate, \
    EmployeeRetriveUpdateDestroy, StoreListCreate, \
    StoreRetriveUpdateDestroy, AnalyticListCreate, \
    AnalyticRetriveUpdateDestroy, AnalyticDisplayListCreate, \
    AnalyticDisplayRetriveUpdateDestroy, \
    TotalDisplayListCreate, TotalDisplayRetriveUpdateDestroy
    #  EmployeeList, EmployeeDetail, EmployeeDetailView2

app_name = 'camera'

urlpatterns = [
    path('', index, name='index'),
    path('organization/', OrganizationListCreate.as_view(), name='category-list'),
    path('organization/<int:pk>', OrganizationRetriveUpdateDestroy.as_view(), name='category-list'),
    # path('employe/', EmployeeList.as_view(), name='employee-list'),
    # path('employe/<int:pk>', EmployeeDetail.as_view(), name='employee-list'),

    # url(r'^employe/$', EmployeeDetail.as_view(), name='employee-list'),
    # re_path(r'^employe/(?P<pk>\d{2})/$', EmployeeDetail.as_view(), name='employee-list'),
    # url('^employ/(?P<pk>[0-9]+)/$', EmployeeDetail.as_view(), name='employee-list'),
    # path('employedetail/', EmployeeDetailView2.as_view(), name='employee-detail2'),


    path('employee/', EmployeeListCreate.as_view(), name='employee-list'),
    path('employee/<int:pk>', EmployeeRetriveUpdateDestroy.as_view(), name='employee-detail'),
    path('store/', StoreListCreate.as_view(), name='store-list'),
    path('store/<int:pk>', StoreRetriveUpdateDestroy.as_view(), name='store-detail'),
    path('analyticsavetodb/', AnalyticListCreate.as_view(), name='analyticsavetodb-list'),
    path('analyticsavetodb/<int:pk>', AnalyticRetriveUpdateDestroy.as_view(), name='analyticsavetodb-detail'),
    path('analyticdisplay/', AnalyticDisplayListCreate.as_view(), name='analyticdisplay-list'),
    path('analyticdisplay/<int:pk>', AnalyticDisplayRetriveUpdateDestroy.as_view(), name='analyticdisplay-detail'),
    path('totaldisplay/', TotalDisplayListCreate.as_view(), name='totaldisplay-list'),
    path('totaldisplay/<int:pk>', TotalDisplayRetriveUpdateDestroy.as_view(), name='totaldisplay-detail'),
    path("usercreate/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]
