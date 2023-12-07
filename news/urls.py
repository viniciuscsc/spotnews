from django.urls import path
from news.views import home, detalhes_noticia, new_category_form

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id_noticia>/", detalhes_noticia, name="news-details-page"),
    path("categories/", new_category_form, name="categories-form"),
]
