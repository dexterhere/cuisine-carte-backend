from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.exceptions import NotFound



class RecipeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, unique_token):
        try:
            return Recipe.objects.get(unique_token=unique_token)
        except (Recipe.DoesNotExist):
            raise NotFound("The recipe is not available")
        

    def get(self, request, unique_token):
        recipe = self.get_object(unique_token)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def put(self, request, unique_token):
        recipe = self.get_object(unique_token)
        serializer = RecipeSerializer(recipe, data=request.data, context={'request':request}, partial=True)

        serializer.validate_recipe_ownership(recipe)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, unique_token):
        recipe = self.get_object(unique_token)
        serializer = RecipeSerializer(context={'request':request})


        serializer.validate_recipe_ownership(recipe)

        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recipes = Recipe.objects.filter(created_by=request.user)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data, context={'request':request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
