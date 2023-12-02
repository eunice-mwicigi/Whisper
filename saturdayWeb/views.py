from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
def home(request):
    return render(request, 'home.html')

from django.core.mail import send_mail
def whispers(request):
    return render(request, 'whispers.html')

def sexualhealth(request):
    return render(request, 'sexual health.html')


def rationale(request):
    return render(request, 'rationale.html')

def contraception(request):
    return render(request, 'contraception.html')

def consentandsexualabuse(request):
    return render(request, 'consent and sexual abuse.html')

def sendemail(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        send_mail(
            'New Submission',
            message,
            '',
            ['whisperdjangoproject@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse('Message sent successfully!')
    return render(request, 'sendemail.html')

def article1(request):
    return render(request, template_name='article1.html')

def article2(request):
    return render(request, template_name='article2.html')

def article3(request):
    return render(request, template_name='article3.html')

# views.py
from django.shortcuts import render
from .models import SexualHealthPost

def sexual_health(request):
    posts = SexualHealthPost.objects.all().order_by('-published_date')
    return render(request, 'sexual health.html', {'posts': posts})
