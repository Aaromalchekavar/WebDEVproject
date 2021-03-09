from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    return render(request, 'webapp/index.html')


def about(request):
    return render(request, 'webapp/about.html')


def contact(request):
    return render(request, 'webapp/contact.html')


def feedback(request):
    return render(request, 'webapp/feedback.html')

def engineering(request):
    engineeringobjects = EngineeringExam.objects.all()
    return render(request, 'webapp/engineering-exams.html', {'engexams': engineeringobjects})

def medical(request):
    medicalexams = MedicalExam.objects.all()
    return render(request, 'webapp/medical-exams.html', {'medexams': medicalexams})

def defence(request):
    defenceexams = DefNavArm.objects.all()
    return render(request, 'webapp/Defence-exams.html', {'defexams': defenceexams})

def search(request):
    query = request.GET['query']
    searchExams = EngineeringExam.objects.filter(name__icontains=query)

    if bool(searchExams) == True:
        print("engineering database has the exam")
        # params = {'searchExams': searchExams}
    elif bool(searchExams) == False:
        print("engineering database doesnt have the exam")
        searchExams = MedicalExam.objects.filter(name__icontains=query)
        if bool(searchExams) == True:
            print("med database has the exam")
            # params = {'searchExams': searchExams}
        elif bool(searchExams) == False:
            print("med database doesnt have the exam ")
            # params = {}

    return render(request, 'webapp/search.html', {'params': searchExams})
    # return render(request, 'webapp/search.html')