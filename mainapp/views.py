from django.shortcuts import render, redirect
from .models import Category, Product, Review
from .forms import CategoryForm, ProductForm, ReviewForm  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
 
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'mainapp/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'mainapp/login.html', {
                'error': "Қате логин немесе пароль"
            })

    return render(request, 'mainapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/home.html', {'categories': categories})

def catalog(request):
    products = Product.objects.all()
    return render(request, 'mainapp/catalog.html', {'products': products})

def catalog_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'mainapp/catalog.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = product.review_set.all()
    return render(request, 'mainapp/product_detail.html', {
        'product': product,
        'reviews': reviews
    })

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'mainapp/add_category.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(request, 'mainapp/add_product.html', {'form': form})

def add_review(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'mainapp/add_review.html', {'form': form, 'product': product})