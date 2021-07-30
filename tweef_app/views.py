from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import UserSerializer
from utils import get_db_handle
from bson import json_util
from datetime import datetime
#https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
#TODO : Buscar como paginar 
class RegisterUser(APIView):
    def post(self, request):
        db_handle, client = get_db_handle('admin', 'localhost', '27017', 'root', 'tabaxco')
        request.data["birthday"] = datetime.strptime(request.data["birthday"], '%d/%m/%y')
        request.data["created_data"] = datetime.now()
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            db_handle.col.insert_one(user_serializer.data)
            return Response(status= status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        db_handle, client = get_db_handle('admin', 'localhost', '27017', 'root', 'tabaxco')
        collection = db_handle.col
        return Response(json_util.dumps(collection.find()) , status=status.HTTP_200_OK)
    