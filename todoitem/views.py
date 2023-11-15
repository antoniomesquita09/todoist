from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todoitem.models import Todoitem
from todoitem.serializers import TodoitemSerializer


# Create your views here.
def single(id_arg):
    try:
        queryset = Todoitem.objects.get(id=id_arg)
        return queryset
    except Todoitem.DoesNotExist:
        return None


class TodoitemView(APIView):
    def get(self, request):
        queryset = Todoitem.objects.all().order_by('created_at')
        serializer = TodoitemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):

        # Mocked author
        request.data['author'] = 1
        serializer = TodoitemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request, id_arg):
        queryset = single(id_arg=id_arg)
        if queryset:
            serializer = TodoitemSerializer(queryset)
            return Response(serializer.data)
        else:
            return Response({'msg': f'Item com id #{id_arg} não encontrado'}, status.HTTP_404_NOT_FOUND)
