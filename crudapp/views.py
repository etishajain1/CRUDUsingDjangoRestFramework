from .models import Studdb
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict

class StudentAllApi(APIView):
    def get(self,request):
        student=Studdb.objects.all().values()
        print(Studdb.objects)
        return Response(student,status=status.HTTP_200_OK)

    # @api_view(['GET'])
    # def view(request):
    #     if request.query_params:
    #         student=Studdb.objects.filter(**request.query_params.dict())
    #     else:
    #         student=Studdb.objects.all().values()
    #     print(student)
    #     return Response(student,status=status.HTTP_200_OK)


class StudentAddApi(APIView):
    def post(self,request):
        data=request.data
        Studdb.objects.create(
            sid=data.get("sid"),
            name=data.get("name"),
            phone=data.get("phone"),
            email=data.get("email"),
            passing_year=data.get("passing_year"),
            finishing_date=data.get("finishing_date"),
            age=data.get("age"),
            address=data.get("address")
        )
        return Response("OK",status=status.HTTP_200_OK)

class StudentDeleteApi(APIView):
    def delete(self,request,id):
        Studdb.objects.get(sid=id).delete()
        return Response({'status':'OK'})

class StudentUpdateApi(APIView):
    def put(self,request,id):
        student=Studdb.objects.get(sid=id)
        student.name=request.data.get("name")
        student.save()
        return Response({'status' : 'OK'})

class StudentGetApi(APIView):
    def get(self,request,id):
        data=Studdb.objects.get(sid=id)
        return Response(
            model_to_dict(data)
        )
        