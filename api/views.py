from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Alert
from .models import Tourist

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

# views.py
@csrf_exempt
@api_view(['POST'])
@authentication_classes([])  # Keep empty for now
@permission_classes([])
def login_user(request):
    data = request.data
    tourist_id = data.get("touristId")
    name = data.get("name")
    phone = data.get("phone")
    user_type = data.get("userType", "tourist")

    if not tourist_id:
        return Response({"error": "touristId is required"}, status=status.HTTP_400_BAD_REQUEST)

    tourist, created = Tourist.objects.get_or_create(
        tourist_id=tourist_id,
        defaults={
            "name": name,
            "phone": phone,
            "user_type": user_type
        }
    )

    return Response({
        "tourist_id": tourist.tourist_id,
        "name": tourist.name,
        "phone": tourist.phone,
        "user_type": tourist.user_type,
        "created": created
    }, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_tourists(request):
    try:
        tourists = Tourist.objects.all().order_by('-created_at')
        data = [{
            "tourist_id": t.tourist_id,
            "name": t.name,
            "phone": t.phone,
            "email": t.email,
            "user_type": t.user_type,
            "created_at": t.created_at
        } for t in tourists]
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
