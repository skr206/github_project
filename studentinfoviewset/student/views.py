from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from student.models import Student
from student.serializers import StudentSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


# Create your views here.
class Student_view(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[AllowAny,]
    # permission_classes=[IsAuthenticated,]
    # permission_classes=[IsAdminUser,]
    # permission_classes=[IsAuthenticatedOrReadOnly,]
    # permission_classes=[DjangoModelPermissions,]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly,]
