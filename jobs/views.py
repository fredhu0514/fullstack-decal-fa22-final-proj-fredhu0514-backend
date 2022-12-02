import json

from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import Job_Get_Serializer, Job_Posting
from .models import Job
from .authentication import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication 


class JobView(viewsets.ModelViewSet):
    serializer_class = Job_Get_Serializer
    queryset = Job.objects.all().order_by("-post_date")
    authentication_classes = [CsrfExemptSessionAuthentication]
    http_method_names = ['get']

    def retrieve(self, request, pk=None, *args, **kwarg):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwarg):
        if len(self.queryset) == 0:
            return Response({}, status=status.HTTP_200_OK)
        return Response(self.serializer_class(self.queryset, many=True).data, status=status.HTTP_200_OK)


class JobCreate(viewsets.ViewSet):
    serializer_class = Job_Posting
    authentication_classes = [CsrfExemptSessionAuthentication]

    http_method_names = ['post']

    def create(self, request, *args, **kwarg):
        print("WTF0")
        user = request.user
        print("USER", user, user.email)
        if not user.is_authenticated:
            return Response(data={"detail": "you have to log in first"}, status=status.HTTP_400_BAD_REQUEST)
        print("WTF1")
        data = {
            "company": request.data.get('company'),
            "refer_scope_link": request.data.get('refer_scope_link'),
            "refer_scope_description": request.data.get('refer_scope_description'),
            "refer_requirement": request.data.get('refer_requirement'),
        }
        print("REQUEST", request.data)
        print("DATA", data)

        err_msg = self.validate_data(data)
        if err_msg:
            print("FUCK the error++++++++++++", err_msg)
            return Response(data={"error": err_msg}, status=status.HTTP_400_BAD_REQUEST)
        print("WTF2")

        data['recommender'] = user.pk

        serializer = self.serializer_class(data=data) #, context={'author': user})
        print("WTF3")

        print("serial", serializer)
        if serializer.is_valid():
            print("WTF4.1")
            serializer.save()
            print("WTF5")
            # instance = Job.objects.filter(id=serializer.data['id']).first()
            # print("WTF6")
            return Response(data={}, status=status.HTTP_201_CREATED)
        else:
            print("WTF4.2")
            print(serializer.errors)
            print("DEBUG ABOVE")
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_data(self, data):
        for key in data:
            if data[key] is None:
                return f"{key} should not be empty"