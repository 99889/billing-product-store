from rest_framework import generics
from .models import Product, Customer, Sale
from .serializers import ProductSerializer, CustomerSerializer, SaleSerializer
from .forms import CustomerForm

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SaleListCreate(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
from django.shortcuts import render

def product_management(request):
    return render(request, 'product_management.html')

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            # Authentication failed, show error message
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    
    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})

from django.shortcuts import render, redirect
from .models import Sale
from .forms import SaleForm

def bill_customer(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            # Assuming you have a Sale model that stores each sale made
            sale = form.save()  # Save the sale record
            total_amount = 0
            # Iterate through the items purchased and calculate the total amount
            for item in sale.items.all():
                total_amount += item.product.price * item.quantity
            # Render the bill template with the necessary information
            return render(request, 'bill_template.html', {'sale': sale, 'total_amount': total_amount})
    else:
        form = SaleForm()
    return render(request, 'bill_customer.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
def customer_management(request):
    customers = Customer.objects.all()
    return render(request, 'customer_management.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_management')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_management')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'update_customer.html', {'form': form, 'customer': customer})
