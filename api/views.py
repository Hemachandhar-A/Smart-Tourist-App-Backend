from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Alert
from .authentication import APIKeyAuthentication
from .serializers import AlertSerializer

# CSRF is disabled for now to simplify dev. Must re-enable later!

# Create your views here.
def hello(req):
    return JsonResponse({"message": "Hello, World!"})

@csrf_exempt
@api_view(['POST'])
@authentication_classes([]) #removed APIKeyAuthentication
@permission_classes([])
def send_alert(req):
    try:
        serializer = AlertSerializer(data=req.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['GET'])
@authentication_classes([])#removed APIKeyAuthentication
@permission_classes([])
def get_alerts(req):
    try:
        alerts = Alert.objects.all()
        data = list(alerts.values())
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        