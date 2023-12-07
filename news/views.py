from django.shortcuts import render
from news.models import News


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def detalhes_noticia(request, id_noticia):
    context = {"new": News.objects.get(id=id_noticia)}
    return render(request, "news_details.html", context)
