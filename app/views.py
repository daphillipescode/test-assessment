import re

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render

from app.models import Contact


def landing(request):
    if request.method == "POST":
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        error = []
        if not re.fullmatch(email_regex, request.POST.get('email')):
            error.append("* Invalid Email Address.")

        if len(request.POST.get('password')) <= 8:
            error.append("* Password must be longer than 8 characters")

        if error:
            return JsonResponse({'error': True, 'msg': error})
        else:
            Contact.objects.create(
                email=request.POST.get('email'),
                password=make_password(request.POST.get('password')),
                colors=request.POST.get('color'),
                animal_list=request.POST.getlist('animals'),
                type=request.POST.get('type') if request.POST.get('type') else None
            )
            return JsonResponse({'data': 'success'})
    context = {
        'title': 'contact'
    }
    return render(request, 'contact.html', context)


def accessibility(request):
    context = {
        'title': 'accessibility'
    }
    return render(request, 'accessibility.html', context)


def progressive_enhancement(request):
    context = {
        'title': 'progressive_enhancement'
    }
    return render(request, 'progressive_enhancement.html', context)


def browser_support(request):
    context = {
        'title': 'browser_support'
    }
    return render(request, 'browser_support.html', context)


def testing(request):
    context = {
        'title': 'testing'
    }
    return render(request, 'testing.html', context)


def documentation(request):
    context = {
        'title': 'documentation'
    }
    return render(request, 'documentation.html', context)