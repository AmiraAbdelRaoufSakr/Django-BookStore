from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from books.models import User
from .serializers import UserSerializer


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "user has been registered successfully"
        }, status=status.HTTP_201_CREATED)
    return Response(data={
            "success": False,
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
