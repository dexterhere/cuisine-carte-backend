from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['unique_token', 'user', 'comment', 'rating', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at', 'unique_token']  # These fields will not be settable by the client

    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment.objects.create(user=user, **validated_data)
        return comment
