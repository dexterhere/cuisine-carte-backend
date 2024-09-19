from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    # Define how recipes are listed in the admin list view
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    
    # Add filters for the sidebar
    list_filter = ('created_by', 'created_at')
    
    # Add a search bar for recipes
    search_fields = ('title', 'description', 'ingredients')
    
    # Define which fields are displayed in the detailed view/edit form
    fieldsets = (
        ('Recipe Info', {'fields': ('title', 'description', 'preparation', 'ingredients', 'image')}),
        ('Metadata', {'fields': ('created_by', 'created_at', 'updated_at')}),
    )
    
    # Ensure that 'created_by', 'created_at', and 'updated_at' are read-only
    readonly_fields = ('created_by', 'created_at', 'updated_at')

# Register the Recipe model with the RecipeAdmin configuration
admin.site.register(Recipe, RecipeAdmin)
