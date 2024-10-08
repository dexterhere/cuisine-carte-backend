from rest_framework import serializers
from .models import Recipe
from accounts.models import User
from rest_framework.exceptions import PermissionDenied, ValidationError

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'unique_token', 'title', 'description', 'preparation', 'ingredients','image', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['updated_at', 'unique_token']

    def create(self, validated_data):
        validated_data['created_by']=self.context['request'].user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('created_by', None)
        return super().update(instance, validated_data)
    

    def validate(self, attrs):
        image = attrs.get('image')
        if image:
            self.validate_image_size(image)
        return attrs
    
    def validate_image_size(self, image):
        max_image_size = 20 * 1024 * 1024
        if image.size > max_image_size:
            raise ValidationError(f"The size of image should be under{max_image_size/(1024*1024)} MB")
    
    def validate_recipe_ownership(self, recipe):
        request_user = self.context['request'].user
        if recipe.created_by != request_user:
            raise PermissionDenied("You don't have permission to modify or delete this recipe.")
        return recipe