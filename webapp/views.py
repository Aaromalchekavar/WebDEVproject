from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'webapp/index.html')


def about(request):
    return render(request, 'webapp/about.html')


def contact(request):
    return render(request, 'webapp/contact.html')


def feedback(request):
    return render(request, 'webapp/feedback.html')
