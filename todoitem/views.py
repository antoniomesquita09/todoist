from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from todoitem.models import Todoitem
from todoitem.serializers import TodoitemSerializer


# Create your views here.
def single(id_arg):
    try:
        queryset = Todoitem.objects.get(id=id_arg)
        return queryset
    except Todoitem.DoesNotExist:
        return None


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def create(request):
    # Mocked author
    request.data['author'] = 1

    # Set create_at and updated_at time now()
    request.data['created_at'] = datetime.now()
    request.data['updated_at'] = datetime.now()

    serializer = TodoitemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
# @renderer_classes((JSONRenderer,))
def find_by_id(request, id_arg):
    queryset = single(id_arg=id_arg)
    if queryset:
        serializer = TodoitemSerializer(queryset)
        return Response(serializer.data)
    else:
        return Response({'msg': f'Item com id #{id_arg} não encontrado'}, status.HTTP_404_NOT_FOUND)


@api_view(('GET',))
def find_all(request):
    queryset = Todoitem.objects.all().order_by('updated_at').reverse()
    serializer = TodoitemSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(('PUT',))
@renderer_classes((JSONRenderer,))
def update(request, id_arg):
    # Find todoitem to update
    todoitem = single(id_arg)
    if todoitem is None:
        return Response({'msg': f'Item com id #{id_arg} não encontrado'}, status.HTTP_404_NOT_FOUND)

    # Mocked author
    request.data['author'] = 1

    request.data['updated_at'] = datetime.utcnow()
    request.data['created_at'] = todoitem.created_at

    serializer = TodoitemSerializer(todoitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def delete(request, id_arg):
    todoitem = single(id_arg=id_arg)
    if todoitem is None:
        return Response({'msg': f'Item com id #{id_arg} não encontrado'}, status.HTTP_404_NOT_FOUND)

    todoitem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
