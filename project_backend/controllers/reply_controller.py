from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from project_backend.models.reply_model import Reply
from ..serializers import Reply_serializer

@api_view(['POST'])
def add(request):
    serializer = Reply_serializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(serializer.errors)


@api_view(['GET'])
def get(request):
    id = request.query_params.get('id')
    try:
        if id:
            user = Reply.objects.get(pk=id)
            serializer = Reply_serializer(user, many=False)
        else:
            users = Reply.objects.all()
            serializer = Reply_serializer(users, many=True)
        return Response(serializer.data)
    except Reply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update(request, pk):
    try:
        user = Reply.objects.get(pk=pk)
    except Reply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = Reply_serializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    print(request.data)
    try:
        user = Reply.objects.get(pk=pk)
    except Reply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)