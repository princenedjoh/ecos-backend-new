from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from project_backend.models.settings_model import Settings
from project_backend.models.users_model import Users
from ..serializers import Settings_serializer, Users_serializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add(request):
    user = Users_serializer(Users.objects.get(username=request.user), many=False)
    request.data['user'] = user.data['id']
    serializer = Settings_serializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data.get('user')
        name = serializer.validated_data.get('name')
        if Settings.objects.filter(user=user, name=name).exists():
            return Response('Setting with this name already exists for this user', status=status.HTTP_409_CONFLICT)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    user = Users_serializer(Users.objects.get(username=request.user), many=False).data['id']
    name = request.query_params.get('name')
    value = request.query_params.get('value')

    filter_criteria = {'user': user}
    if name:
        filter_criteria['name'] = name
    if value:
        filter_criteria['value'] = value

    try:
        settings = Settings.objects.filter(**filter_criteria)
        serializer = Settings_serializer(settings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def search(request):
    user = request.query_params.get('user')
    name = request.query_params.get('name')
    value = request.query_params.get('value')

    filter_criteria = {}
    if user:
        filter_criteria['user'] = user
    if name:
        filter_criteria['name'] = name
    if value:
        filter_criteria['value'] = value

    try:
        settings = Settings.objects.filter(**filter_criteria)
        serializer = Settings_serializer(settings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request):
    user = Users_serializer(Users.objects.get(username=request.user), many=False)
    name = request.query_params.get('name')
    id = user.data['id']
    request.data['user'] = id

    filter_criteria = {'user': id}
    if name:
        filter_criteria['name'] = name
        request.data['name'] = name
        print(request.data)
    if not name:
        return Response('Please input a name param', status=status.HTTP_400_BAD_REQUEST)
    
    settings = Settings.objects.filter(**filter_criteria)
    
    if not settings.exists():
        user = Users_serializer(Users.objects.get(username=request.user), many=False)
        request.data['user'] = user.data['id']
        serializer = Settings_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            name = serializer.validated_data.get('name')
            if Settings.objects.filter(user=user, name=name).exists():
                return Response('Setting with this name already exists for this user', status=status.HTTP_409_CONFLICT)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    serializer = Settings_serializer(settings[0], data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request, pk):
    print(request.data)
    try:
        user = Settings.objects.get(pk=pk)
    except Settings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)