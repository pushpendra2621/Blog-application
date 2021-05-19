from BlogApp.forms import ContactForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from BlogApp.models import Post, Category, Tag, Contact
from BlogApp.forms import *
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def index(request):
    articles = Post.objects.filter(status="published").order_by('-published_date')
    categories = Category.objects.all()
    template = loader.get_template('index.html')
   
    #search
    query= request.GET.get('q')
    if query is not None:
        lookups= Q(title__icontains=query) | Q(content__icontains=query)
        articles= articles.filter(lookups).distinct()

    #pagination
    paginator = Paginator(articles, 6)#show 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "articles":page_obj,
        "categories": categories
    }
    return HttpResponse(template.render(context, request))

def category(request, category_slug): #this category_slug is coming from the template.
    articles = Post.objects.filter(status="published").order_by('-published_date')
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug) #the slug we obtained with request from the template will replace the slug field of model Category and get store in category.
        articles = articles.filter(category=category)
    
    #search
    query= request.GET.get('q')
    if query is not None:
        lookups= Q(title__icontains=query) | Q(content__icontains=query)
        articles= articles.filter(lookups).distinct()

    #pagination
    paginator = Paginator(articles, 6)#show 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "articles":page_obj,
        "category": category,
        "categories": categories
    }
    return render(request, "category.html",context=context)

def tag(request, tag_slug):
    categories = Category.objects.all()
    tag = Tag.objects.all()
    articles = Post.objects.filter(status="published").order_by('-published_date')
    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        articles = articles.filter(tag=tag)

     #search
    query= request.GET.get('q')
    if query is not None:
        lookups= Q(title__icontains=query) | Q(content__icontains=query)
        articles= articles.filter(lookups).distinct()

    #pagination
    paginator = Paginator(articles, 6)#show 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "articles":page_obj,
        "tag" : tag,
        "categories": categories,
    }
    return render(request, "tag.html",context=context)

def PostDetails(request, post_slug):
    categories = Category.objects.all()
    articles = get_object_or_404(Post, slug = post_slug)

    context = {
        "articles":articles,
        "categories": categories,
    }
    return render(request, "post_page.html", context=context)

def messages(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.msg_date = timezone.now()
            message.save()
            return redirect('messagesuccess')
    else :
        form = ContactForm()
        
    return render(request, 'message.html', {"form":form})

def MessageSuccess(request):
    return render(request, 'messagesuccess.html')

        
            
            

    