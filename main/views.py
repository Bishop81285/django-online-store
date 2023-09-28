from django.shortcuts import render, get_object_or_404

from main.models import Product, Contact


def index(request):
    products = Product.objects.all()[:6]
    context = {'object_list': products}
    return render(request, 'main/index.html', context)


def contacts(request):
    contacts_list = Contact.objects.first()
    context = {
        'object_list': contacts_list,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"{name}({email}):{message}")

    return render(request, 'main/contacts.html', context)


def product(request, pk):
    products_list = get_object_or_404(Product, pk=pk)
    context = {
        'object_list': products_list,
    }

    return render(request, 'main/product.html', context)
