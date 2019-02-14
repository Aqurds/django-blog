from django.shortcuts import render

# Create your views here.



items = [
    {
    'author': 'Omar',
    'title': 'First blog post',
    'content': 'First blog post content',
    'date_posted': 'January 17, 2019'
    },
    {
    'author': 'Nupur',
    'title': 'Second blog post',
    'content': 'Second blog post content',
    'date_posted': 'January 21, 2019'
    }
]


def home(request):
    context = {
        'posts': items,
        'title': 'Django Blog - Home'
    }
    return render(request, 'ecommerce/home.html')


def about(request):
    return render(request, 'ecommerce/about.html', {'title': 'Django Blog - About Page'})


def contact(request):
    return render(request, 'ecommerce/contact.html', {'title': 'Django Blog - About Page'})
