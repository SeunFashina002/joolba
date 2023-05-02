from django.urls import path

from Search.views import SearchArticles, SearchCategories

urlpatterns = [
    path('category/<str:query>/', SearchCategories.as_view()),
    path('article/<str:query>/', SearchArticles.as_view()),
]