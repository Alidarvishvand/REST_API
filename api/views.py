


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import person,question,answer
from .serializers import personserializer,Questionserializer,AnswerSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from permission import IsOwnerOrReadOnly
#home classes ==>
class HOME(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny,]
    def get(self,request):
        
        persons = person.objects.all()
        ser_data = personserializer(instance=persons,many = True)
        return Response(data=ser_data.data)


#classes question==>
class Questionlistview(APIView):
    def get(self,request):
        questions = question.objects.all()
        srz_data = Questionserializer(instance=questions, many = True).data
        return Response(srz_data,status=status.HTTP_200_OK)
    
    
class questioncreatview(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self,request):
        srz_data = Questionserializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class questionupdateview(APIView):
        permission_classes = [IsOwnerOrReadOnly,]


        def put(self,request,pk):
            questions = question.objects.get(pk=pk)
            self.check_object_permissions(request,questions)
            srz_data = Questionserializer(instance=questions,data=request.data, partial=True)
            if srz_data.is_valid():
                srz_data.save()
                return Response(srz_data.data, status=status.HTTP_200_OK)
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
class questiondeletview(APIView):
     permission_classes = [IsOwnerOrReadOnly,]
     def delete(self,request,pk):
        questions = question.objects.get(pk=pk)
        questions.delete()
        return Response({'message':'questions deleted successfully'},status=status.HTTP_200_OK)
    
