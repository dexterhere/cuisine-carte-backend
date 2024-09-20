from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    # Define how comments are listed in the admin list view
    list_display = ('user', 'comment', 'rating', 'created_at', 'updated_at')
    
    # Add filters for the sidebar
    list_filter = ('user', 'rating', 'created_at')
    
    # Add a search bar for comments
    search_fields = ('comment', 'user__username')
    
    # Define which fields are displayed in the detailed view/edit form
    fieldsets = (
        ('Comment Info', {'fields': ('user', 'comment', 'rating')}),
        ('Metadata', {'fields': ('created_at', 'updated_at')}),
    )
    
    # Ensure that 'created_at' and 'updated_at' are read-only
    readonly_fields = ('created_at', 'updated_at')

# Register the Comment model with the CommentAdmin configuration
admin.site.register(Comment, CommentAdmin)
