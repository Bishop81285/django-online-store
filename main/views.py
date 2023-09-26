import os

from django.shortcuts import render

from main.models import Product


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    print(latest_products)

    return render(request, 'main/home.html')


def save_feedback(data):
    feedbacks_path = os.path.join(os.path.dirname(__file__), 'feedbacks')
    feedback_file = open(os.path.join(feedbacks_path, 'feedback.txt'), 'a')

    feedback_file.write(f"{data['name']}, {data['phone']}, {data['message']}\n")

    feedback_file.close()


def contacts(request):
    if request.method == 'POST':
        data = request.POST
        save_feedback(data)

    return render(request, 'main/contacts.html')
