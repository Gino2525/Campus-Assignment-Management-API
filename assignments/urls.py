from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentLoginView, AssignmentViewSet,StudentRegisterView,home

router = DefaultRouter()
router.register("assignments", AssignmentViewSet, basename="assignments")

urlpatterns = [
    path("", home),
    path("login/", StudentLoginView.as_view()),
    path("register/", StudentRegisterView.as_view()),
    path("", include(router.urls)),
]