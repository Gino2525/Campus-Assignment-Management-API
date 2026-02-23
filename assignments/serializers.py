from rest_framework import serializers
from .models import Student
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from .models import Assignment


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["username", "name", "email", "password", "department", "year"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
class StudentLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            student = Student.objects.get(username=data["username"])
        except Student.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not student.check_password(data["password"]):
            raise serializers.ValidationError("Invalid credentials")

        data["student"] = student
        return data



class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"
        read_only_fields = ("student",)

