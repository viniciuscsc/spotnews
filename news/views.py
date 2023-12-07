from django.shortcuts import render, redirect
from news.models import News, Category
from news.forms import NewCategoryForm


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def detalhes_noticia(request, id_noticia):
    context = {"new": News.objects.get(id=id_noticia)}
    return render(request, "news_details.html", context)


def new_category_form(request):
    form = NewCategoryForm()

    if request.method == "POST":
        form = NewCategoryForm(request.POST)

    if form.is_valid():
        Category.objects.create(**form.cleaned_data)
        return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)
