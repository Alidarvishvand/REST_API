


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import person 
from .serializers import personserializer

class HOME(APIView):
    def get(self,request):
        # name= request.query_params['name']
        persons = person.objects.all()
        ser_data = personserializer(instance=persons,many = True)
        return Response(data=ser_data.data)
    

    # def post(self,request):
    #     name = request.data['name']
    #     return Response({'name':name})