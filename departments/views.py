from django.http import *
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins

from departments.models import Department
from departments.serializers import *


class DepartmentListAPIView(APIView):

    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentListSerializer(departments, many=True)
        return Response(serializer.data)

class DepartmentDetailApiAPIView(APIView):

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentDetailSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentDetailSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDepartmentAPIView(APIView):

    permission_classes = (AllowAny, )

    def post(self, request):
        department = request.data
        serializer = CreateDepartmentSerializer(data=department)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data,
                        status=status.HTTP_201_CREATED)


class DepartmentDetailAPIView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  queryset = Department.objects.all()
  serializer_class = DepartmentDetailSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
