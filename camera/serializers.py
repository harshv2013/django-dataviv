from rest_framework import serializers
from datetime import datetime
from camera.models import Employee, Organization, Store, User, \
    Analytic, AnalyticDisplay, TotalDisplay, Client, \
    AnalyticEntry, TestUser, EmployeeMedia, Attendence, \
    AttendenceMedia, Analysis1, Analysis2, ModelAnalysis, \
    StoreImage
    


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


class EmployeeAttendenceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    attendences = serializers.SerializerMethodField('get_attendences')

    def get_attendences(self, obj):
        # dt = self.request.query_params.get('dt', None)
        dt = self.context.get('dt',None)
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',dt)
        # dt = "2020-10-08"
        # dt = datetime.strptime(dt, '%Y-%m-%d').date()
        # date_at = instance.objects.filter(created_at.date==dt)
        if dt:
            attendences = AttendenceSerializer2(Attendence.objects.filter(employee=obj).filter(created_at__date=dt),many=True).data
        else:
            attendences = AttendenceSerializer2(Attendence.objects.filter(employee=obj),many=True).data

        return attendences


    class Meta:
        model = Employee
        # fields = "__all__"
        fields = ['id', 'name', 'store', 'owner', 'attendences']
###############################################

###############################################


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = "__all__"

class AttendenceSerializer2(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M:%S")
    date_at = serializers.SerializerMethodField(method_name='get_date')
    # date_at = serializers.DateTimeField(format="%H:%M:%S")
    class Meta:
        model = Attendence
        fields = ['id', 'created_at', 'date_at']

    def get_date(self, instance):
        data_at = instance.created_at.date()
        # data_at = instance.get(created_at.date==dt)
        # dt = "2020-10-08"
        # dt = datetime.strptime(dt, '%Y-%m-%d').date()
        # date_at = instance.objects.filter(created_at.date==dt)

        # if obj.get("product_id"):
        #     obj_product = Product.objects.filter(id=obj.get("product_id")).first()
        # request = self.context.get('request')
        # user = request.user
        # if user.is_authenticated() and user.is_staff:
        #     return datetime.datetime.now().year - instance.dob.year
        return data_at


class EmployeeSerializer2(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    attendences = AttendenceSerializer2(many=True, read_only=True)

    class Meta:
        model = Employee
        # fields = "__all__"
        fields = ['id', 'name','email', 'contact', 'gender', 'age', 'address', 'employee_media', 'embedding', 'store', 'owner', 'attendences']


class EmployeeSerializer3(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # attendences = AttendenceSerializer2(many=True, read_only=True)

    attendences = serializers.SerializerMethodField('get_attendences')

    def get_attendences(self, obj):
        # dt = self.request.query_params.get('dt', None)
        dt = self.context.get('dt',None)
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',dt)
        # dt = "2020-10-08"
        # dt = datetime.strptime(dt, '%Y-%m-%d').date()
        # date_at = instance.objects.filter(created_at.date==dt)
        if dt:
            attendences = AttendenceSerializer2(Attendence.objects.filter(employee=obj).filter(created_at__date=dt),many=True).data
        else:
            attendences = AttendenceSerializer2(Attendence.objects.filter(employee=obj),many=True).data

        return attendences

        # StudentSerializer(
        #             Student.objects.filter(college_id=self.college_id),
        #             many=True
        #         ).data


    class Meta:
        model = Employee
        # fields = "__all__"
        fields = ['id', 'name','email', 'contact', 'gender', 'age', 'address', 'employee_media', 'embedding', 'store', 'owner', 'attendences']



class EmployeeMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMedia
        fields = "__all__"
##########################################################


# class AttendenceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendence
#         fields = "__all__"
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

class StoreImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreImage
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    storeimage = StoreImageSerializer()
    class Meta:
        model = Store
        # fields = "__all__"
        fields = ["id", "location", "total_camera", "outer_camera_channel_no", 
                  "billing_camera_channel_no", "camera_sequence" , "organization","storeimage" ]

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


class ModelAnalysisSerializer3(serializers.ModelSerializer):
    timeinhms = serializers.SerializerMethodField() #Custom serializer method

    def get_timeinhms(self, obj):
        timeinhms = obj.timestamp.time()
        return timeinhms

    class Meta:
        model = ModelAnalysis
        # fields = "__all__"
        fields = ['id', 'img_url', 'classtype', 'updatedclasstype', 'flag', 'store','timestamp','timeinhms']
        # read_only_fields = ['timeinhms']