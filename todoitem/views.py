from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todoitem.models import Todoitem
from todoitem.serializers import TodoitemSerializer


# Create your views here.
class TodoitemView(APIView):
    def get(self, request):
        queryset = Todoitem.objects.all().order_by('created_at')
        serializer = TodoitemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response({'msg': 'Resposta do método POST'}, status.HTTP_200_OK)
