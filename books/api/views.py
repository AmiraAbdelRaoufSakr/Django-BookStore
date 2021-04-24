from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer, ShowBookSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(instance=books, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "New Book has been added successfully"
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "error": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(data={"Book doesnot found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Book has been updated successfully"
        }, status=status.HTTP_200_OK)
    return Response(data={
        "success": False,
        "error": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def show(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(data={"Book doesnot found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ShowBookSerializer(instance=book)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(data={"Book doesnot found"}, status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response(data={"Book has been deleted successfully"}, status=status.HTTP_200_OK)
