from ast import Or
import re
from tkinter import PAGES
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from wscubetech.forms import usersForm
from service.models import Service
from news.models import News


# Home Page 
def homePage(request):
    # data = {
    #     'title': 'Home New',
    #     'bdata': 'Welcome to Wscubetech',
    #     'clist': ['PHP', 'Java', 'Django'],
    #     'numbers': [10,20,30,40,50],
    #     'student_details': [           
    #         {'name': 'Uday Jio', 'phone': 8511217185},
    #         {'name': 'Uday Idea', 'phone': 7202009625}
    #     ]
    # }
    newsData = News.objects.all()
    servicesData = Service.objects.all().order_by("-service_title") # [2:5]
    
    data = {
        'servicesData' : servicesData,
        'newsData' : newsData
    }
    return render(request, "index.html", data)

# News Details
def newsDetails(request, slug):
    print(slug)
    newsDetails = News.objects.get(news_slug=slug)
    data = {
        newsDetails : newsDetails,
    }
    return render(request, "newsdetails.html", data)

# About Page
def about(request):
    return render(request, "about.html")

# Service Page
def service(request):
    servicesData = Service.objects.all().order_by("-service_title") # [2:5]

    # Search
    if request.method == "GET":
        st = request.GET.get('servicename')
        if st != None:
            
            # Exact Search
            # servicesData = Service.objects.filter(service_title = st) 

            # Related Search [Character]
 
                 # __icontains - Search using one letter
            servicesData = Service.objects.filter(service_title__icontains = st)
            
            # Query - Select * from Service where service_title = user input

    # for a in servicesData:
    #     print(a.service_icon)
    
    data = {
        'servicesData' : servicesData
    }

    return render(request, "service.html", data)

# Gallery Page
def gallery(request):
    return render(request, "gallery.html")

# FAQ Page
def faq(request):
    return render(request, "faq.html")

# Contact Page
def contact(request):
    return render(request, "contact.html")

# Thank You
def thankyou(request):
    if request.method == "GET":
        output = request.GET.get('output')

    return render(request, "thankyou.html", {'output': output})

# Elements Page
def elements(request):
    return render(request, "elements.html")

# Generic Page
def generic(request):
    return render(request, "generic.html")

# User Form
def userForm(request):
    # GET
    # finalans = 0
    # try:
    #     # n1 = int(request.GET['num1'])
    #     # n2 = int(request.GET['num2'])
    #     # finalans = n1 + n2

    #             # OR
    #     n1 = int(request.GET.get('num1'))
    #     n2 = int(request.GET.get('num2'))
    #     finalans = n1 + n2
    # except:
    #     pass

    # POST
    # finalans = 0
    # data = {}
    # try:
    #     if request.method == "POST":
    #         n1 = int(request.POST.get('num1'))
    #         n2 = int(request.POST.get('num2'))
    #         finalans = n1 + n2
    #         data = {
    #             'n1' : n1,
    #             'n2' : n2,
    #             'output' : finalans
    #         }
    #         url = "/thankyou/?output={}".format(finalans)
    #         # return HttpResponseRedirect(url)
    #             # OR 
    #         return redirect(url)

    # except:
    #     pass

    # return render(request, "userform.html", data)

    # Form Tutorial
    finalans = 0
    # For display data in textfields
    fn = usersForm()
    data = {'form': fn}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            data = {
                'form' : fn,
                'output' : finalans
            }
            url = "/thankyou/?output={}".format(finalans)
            # return HttpResponseRedirect(url)
                # OR 
            return redirect(url)

    except:
        pass

    return render(request, "userform.html", data)

# Calculator
def calculator(request):
    c = ''

    try:
        if request.method == "POST":
            
            n1 = eval(request.POST.get('num1'))
            opr = request.POST.get('opr')
            n2 = eval(request.POST.get('num2'))

            if opr == "+":
                c = n1+n2
            elif opr == "-":
                c = n1-n2
            elif opr == "*":
                c = n1*n2
            elif opr == "/":
                c = n1/n2

    except:
        c = "Invalid"
    
    print(c)
    return render(request, "calculator.html", {'c': c})

# Save EvenOdd
def saveevenodd(request):
    c = ''
    if request.method == "POST":
        if request.POST.get('num1')=="":
            return render(request, "evenodd.html", {'error': True}) 

        n = eval(request.POST.get('num1'))
        if n % 2 == 0:
            c = "Even Number"
        else:
            c = "Odd Number"
    return render(request, "evenodd.html", {'c': c})

# Marksheet
def marksheet(request):
    try:
        if request.method == "POST":
            s1 = eval(request.POST.get('subject1'))
            s2 = eval(request.POST.get('subject2'))
            s3 = eval(request.POST.get('subject3'))
            s4 = eval(request.POST.get('subject4'))
            s5 = eval(request.POST.get('subject5'))
            
            # Total
            t = s1+s2+s3+s4+s5
            
            # Percentage
            p = t*100/500

            # Division
            if p >= 60:
                d = "First"
            elif p >= 48:
                d = "Second"
            elif p >= 35:
                d = "Third"
            else:
                d = "Fail"

            data = {
                'total': t,
                'percentage': p,
                'division': d
            }
            return render(request, "marksheet.html", data)
    except:
        pass
    return render(request, "marksheet.html")


# Submit
def submitform(request):
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            data = {
                'n1' : n1,
                'n2' : n2,
                'output' : finalans
            }
            return HttpResponse(finalans)
    except:
        pass