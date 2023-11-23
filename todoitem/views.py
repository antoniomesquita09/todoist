from datetime import datetime

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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


common_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING),
        'description': openapi.Schema(type=openapi.TYPE_STRING),
        'done': openapi.Schema(type=openapi.TYPE_BOOLEAN),
    }
)

@swagger_auto_schema(method='POST', request_body=common_request_body)
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


page_param = openapi.Parameter(
    'page', openapi.IN_QUERY,
    description="current page for pagination",
    type=openapi.TYPE_INTEGER
)
total_items_param = openapi.Parameter(
    'total_items', openapi.IN_QUERY,
    description="total items for pagination",
    type=openapi.TYPE_INTEGER
)
order_by_param = openapi.Parameter(
    'order_by', openapi.IN_QUERY,
    description="order for pagination",
    type=openapi.TYPE_STRING
)
filter_by_done_param = openapi.Parameter(
    'filter_by_done', openapi.IN_QUERY,
    description="filter by done items",
    type=openapi.TYPE_BOOLEAN
)


@swagger_auto_schema(method='GET', manual_parameters=[
    page_param,
    total_items_param,
    order_by_param,
    filter_by_done_param
])
@api_view(('GET',))
def find_all(request):
    page = request.GET.get('page', 1)
    total_items = request.GET.get('total_items', 10)
    order_by = request.GET.get('order_by', 'updated_at')
    filter_by_done = request.GET.get('filter_by_done', None)

    page = int(page)
    total_items = int(total_items)

    offset = total_items * (page - 1)
    limit = total_items * page

    queryset = Todoitem.objects.all()

    if filter_by_done is not None:
        filter_by_done_value = True if filter_by_done == 'true' else False
        print(filter_by_done_value)
        queryset = queryset.filter(done__exact=filter_by_done_value)

    queryset = queryset.order_by(order_by).reverse()[offset:limit]
    serializer = TodoitemSerializer(queryset, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='PUT', request_body=common_request_body)
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
