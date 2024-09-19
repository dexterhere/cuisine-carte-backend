from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crud_recipe.views import RecipeDetailView, RecipeListView

urlpatterns = [
    path('recipes/',RecipeListView.as_view(), name="recipe_list"),
    path('recipies/<uuid:unique_token>/',RecipeDetailView.as_view(), name='recipe-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
