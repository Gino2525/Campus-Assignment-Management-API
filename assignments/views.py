from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import StudentLoginSerializer,AssignmentSerializer,StudentRegisterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Assignment
from django.shortcuts import render

def home(request):
    return render(request, "index.html")


class StudentRegisterView(APIView):

    def post(self, request):
        serializer = StudentRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student registered successfully"}, status=201)

        return Response(serializer.errors, status=400)


class StudentLoginView(APIView):

    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)

        if serializer.is_valid():
            student = serializer.validated_data["student"]

            refresh = RefreshToken()
            refresh["student_id"] = student.id

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Assignment.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)