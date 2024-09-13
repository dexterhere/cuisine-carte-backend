from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.exceptions import NotFound



class RecipeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except (Recipe.DoesNotExist):
            raise NotFound("The recipe is not available")
        
    
    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data, context={'request':request})

        serializer.validate_recipe_ownership(recipe)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(context={'request':request})


        serializer.validate_recipe_ownership(recipe)

        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
