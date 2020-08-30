from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
# from rest_framework import status
# from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.models import Token
from camera.models import Employee, Organization, Store, User, \
    Analytic, AnalyticDisplay, TotalDisplay
from camera.permissions import IsOwnerOrReadOnly
from camera.serializers import EmployeeSerializer, \
    UserSerializer, OrganizationSerializer, StoreSerializer, \
    AnalyticSerializer, AnalyticDisplaySerializer, TotalDisplaySerializer






def index(request):
    return HttpResponse("Hello, world. You're at the dataviv index.")

##########################################################################


class OrganizationListCreate(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class OrganizationRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

##########################################################################


class EmployeeListCreate(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        print('in get list ------',request.query_params.get('pk', None))
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRetriveUpdateDestroy(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('pk-------------',pk)
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = Employee(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = Employee(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

###################################################################################

# class EmployeeListCreate(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

##########################################################################
class StoreListCreate(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

#####

##########################################################################


class AnalyticListCreate(generics.ListCreateAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer


class AnalyticRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer


##########################################################################
class AnalyticDisplayListCreate(generics.ListCreateAPIView):
    queryset = AnalyticDisplay.objects.all()
    serializer_class = AnalyticDisplaySerializer


class AnalyticDisplayRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnalyticDisplay.objects.all()
    serializer_class = AnalyticDisplaySerializer

#########################################################################


class TotalDisplayListCreate(generics.ListCreateAPIView):
    queryset = TotalDisplay.objects.all()
    serializer_class = TotalDisplaySerializer


class TotalDisplayRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TotalDisplay.objects.all()
    serializer_class = TotalDisplaySerializer


##########################################################################
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print('request.data----------',request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print('balfdfffffffffffffffffffffffffffff',serializer.instance)
        # user = serializer.data['username']
        # user = User.objects.get(pk=pk_of_user_without_token)
        token = Token.objects.create(user=serializer.instance)
        print('token---------------------', token)
        print('serializer.data in UserCreate in create defn is-', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView2(APIView):
    permission_classes = ()

    def post(self, request,):
        pk = request.data.get("pk")
        print('id is ------------',pk)
        employee = Employee.objects.get(pk=pk)
        print('employee----',employee)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
