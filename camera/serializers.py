from rest_framework import serializers
from camera.models import Employee, Organization, Store, User, \
    Analytic, AnalyticDisplay, TotalDisplay, Client, \
    AnalyticEntry, TestUser, EmployeeMedia, Attendence, \
    AttendenceMedia, Analysis1, Analysis2, ModelAnalysis
    


########################################################

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
#########################################################


class TestUserSerializer(serializers.ModelSerializer):
    # media = serializers.FileField()
    class Meta:
        model = TestUser
        fields = "__all__"
        # fields = ["media"]

#########################################################


class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Employee
        # fields = "__all__"
        fields = ['id', 'name','email', 'contact', 'gender', 'age', 'address', 'employee_media', 'embedding', 'store', 'owner']


class EmployeeMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMedia
        fields = "__all__"
##########################################################


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = "__all__"
##########################################################


class AttendenceMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendenceMedia
        fields = "__all__"
##########################################################


class AnalyticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytic
        fields = "__all__"
##########################################################


class AnalyticDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticDisplay
        fields = "__all__"
##########################################################


class TotalDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalDisplay
        fields = "__all__"
##########################################################


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

##########################################################


class AnalyticEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticEntry
        fields = "__all__"

##########################################################


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


###########################################################
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'is_superuser', 'is_staff', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff'],
            email=validated_data['email']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


################################################################

class Analysis1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis1
        fields = "__all__"


class Analysis2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis2
        fields = "__all__"

################################################################


class ModelAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelAnalysis
        fields = "__all__"

################################################################


class ModelAnalysisSerializer2(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%H:%M:%S")

    class Meta:
        model = ModelAnalysis
        # fields = "__all__"
        fields = ['id', 'img_url', 'classtype', 'updatedclasstype', 'flag', 'store','timestamp']

#######################################################################################################

# class ModelAnalysisTimeSerializer(serializers.ModelSerializer):
#     timeinhms = 

#     class Meta:
#         model = ModelAnalysis
#         fields = ['timestamp', 'timeinhms']


# class ModelAnalysisSerializer3(serializers.ModelSerializer):
#     timeinhms = serializers.DateTimeField(ModelAnalysisSerializer('timestamp'),format="%H:%M:%S")

#     class Meta:
#         model = ModelAnalysis
#         # fields = "__all__"
#         fields = ['id', 'img_url', 'classtype', 'updatedclasstype', 'flag', 'store','timestamp','timeinhms']
#         read_only_fields = ['timeinhms']