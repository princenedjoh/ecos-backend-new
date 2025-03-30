from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from project_backend.models.alert_model import Alert
from ..serializers import Alert_serializer, Users_serializer
from rest_framework.permissions import IsAuthenticated
from project_backend.models.users_model import Users
from datetime import date, datetime
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def add(request, user_id):
    try:
        request_data = request.data.copy()  # Make sure the data is mutable
        request_data['user'] = user_id
        request_data['date'] = datetime.now()
        
        serializer = Alert_serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Invalid serializer data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"detail": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    user_data = Users_serializer(Users.objects.get(username=request.user), many=False)

    user = user_data.data['id']
    id = request.query_params.get('id')
    title = request.query_params.get('title')
    description = request.query_params.get('description')
    date = request.query_params.get('date')
    read = request.query_params.get('read')
    severity = request.query_params.get('severity')
    category = request.query_params.get('category')

    filter_criteria = {'user': user}
    if title:
        filter_criteria['title'] = title
    if description:
        filter_criteria['description'] = description
    if date:
        filter_criteria['date'] = date
    if read:
        filter_criteria['read'] = read
    if severity:
        filter_criteria['severity'] = severity
    if category:
        filter_criteria['category'] = category
    if id:
        filter_criteria['id'] = id

    try:
        alert = Alert.objects.filter(**filter_criteria)
        print(alert)
        serializer = Alert_serializer(alert, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search(request):
    id = request.query_params.get('id')
    try:
        if id:
            user = Alert.objects.get(pk=id)
            serializer = Alert_serializer(user, many=False)
        else:
            users = Alert.objects.all()
            serializer = Alert_serializer(users, many=True)
        return Response(serializer.data)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request):
    user_data = Users_serializer(Users.objects.get(username=request.user), many=False)
    request.data['user'] = user_data.data['id']

    user = user_data.data['id']
    title = request.query_params.get('title')
    description = request.query_params.get('description')
    date = request.query_params.get('date')
    read = request.query_params.get('read')
    severity = request.query_params.get('severity')
    category = request.query_params.get('category')

    filter_criteria = {'user': user}
    if title:
        filter_criteria['title'] = title
    if description:
        filter_criteria['description'] = description
    if date:
        filter_criteria['date'] = date
    if read:
        filter_criteria['read'] = read
    if severity:
        filter_criteria['severity'] = severity
    if category:
        filter_criteria['category'] = category
    
    alert = Alert.objects.filter(**filter_criteria)
    serializer = Alert_serializer(alert[0], data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    user = Users_serializer(Users.objects.get(username=request.user), many=False)
    try:
        user = Alert.objects.get(user=user.data['id'], pk=pk)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)