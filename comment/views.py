from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Comment
from .serializers import CommentSerializer



class CommentDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_object(self, unique_token):
        try:
            return Comment.objects.get(unique_token=unique_token)
        except Comment.DoesNotExist:
            raise NotFound("The comment you are looking for is not available")
        
    def get(self, request, unique_token):
        comment = self.get_object(unique_token)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, unique_token):
        comment = self.get_object(unique_token)
        if comment.user != request.user:
            raise PermissionDenied("You are not authorized to edit this comment.")
        
        serializer = CommentSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def delete(self, request, unique_token):
        comment = self.get_object(unique_token)

        if comment.user != request.user:
            raise PermissionDenied("You are not authorized to delete this comment")
        
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CommentListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)