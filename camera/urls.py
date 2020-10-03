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
    TotalDisplayListCreate, TotalDisplayRetriveUpdateDestroy, \
    ClientListCreate, ClientRetriveUpdateDestroy, \
    AnalyticEntryListCreate, AnalyticEntryRetriveUpdateDestroy,\
    TestUserListCreate, TestUserRetriveUpdateDestroy, \
    EmployeeMediaListCreate, AttendenceListCreate, \
    AttendenceRetriveUpdateDestroy, \
    Analysis1ListCreate, Analysis1RetriveUpdateDestroy, \
    Analysis2ListCreate, Analysis2RetriveUpdateDestroy, \
    ModelAnalysisListCreate, ModelAnalysisRetriveUpdateDestroy, \
    AnalyticData
    
    # TestUserListCreate, TestUserRetriveUpdateDestroy
    #  EmployeeList, EmployeeDetail, EmployeeDetailView2

app_name = 'camera'

urlpatterns = [
    path('', index, name='index'),
    path('organization/', OrganizationListCreate.as_view(), name='category-list'),
    path('organization/<int:pk>', OrganizationRetriveUpdateDestroy.as_view(), name='category-detail'),
    # path('employe/', EmployeeList.as_view(), name='employee-list'),
    # path('employe/<int:pk>', EmployeeDetail.as_view(), name='employee-list'),

    # url(r'^employe/$', EmployeeDetail.as_view(), name='employee-list'),
    # re_path(r'^employe/(?P<pk>\d{2})/$', EmployeeDetail.as_view(), name='employee-list'),
    # url('^employ/(?P<pk>[0-9]+)/$', EmployeeDetail.as_view(), name='employee-list'),
    # path('employedetail/', EmployeeDetailView2.as_view(), name='employee-detail2'),

    path('testuser/', TestUserListCreate.as_view(), name='testuser-list'),
    path('employeemedia/', EmployeeMediaListCreate.as_view(), name='employeemedia-list'),
    path('testuser/<int:pk>', TestUserRetriveUpdateDestroy.as_view(), name='testuser-detail'),


    path('employee/', EmployeeListCreate.as_view(), name='employee-list'),
    path('employee/<int:pk>', EmployeeRetriveUpdateDestroy.as_view(), name='employee-detail'),

    path('attendence/', AttendenceListCreate.as_view(), name='attendence-list'),
    path('attendence/<int:pk>', AttendenceRetriveUpdateDestroy.as_view(), name='attendence-detail'),

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

    path('client/', ClientListCreate.as_view(), name='client-list'),
    path('client/<int:pk>', ClientRetriveUpdateDestroy.as_view(), name='client-detail'),
    
    path('analyticentry/', AnalyticEntryListCreate.as_view(), name='analyticentry-list'),
    path('analyticentry/<int:pk>', AnalyticEntryRetriveUpdateDestroy.as_view(), name='analyticentry-detail'),

    path('analysis1/', Analysis1ListCreate.as_view(), name='analysis1-list'),
    path('analysis1/<int:pk>', Analysis1RetriveUpdateDestroy.as_view(), name='analysis1-detail'),

    path('analysis2/', Analysis2ListCreate.as_view(), name='analysis2-list'),
    path('analysis2/<int:pk>', Analysis2RetriveUpdateDestroy.as_view(), name='analysis2-detail'),

    path('modelanalysis/', ModelAnalysisListCreate.as_view(), name='modelanalysis-list'),
    path('modelanalysis/<int:pk>', ModelAnalysisRetriveUpdateDestroy.as_view(), name='modelanalysis-detail'),

    path('analyticdata/', AnalyticData.as_view(), name='analyticdata-list'),

    
]
