from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Project

def home(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        
        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email='lalmohit167@gmail.com',
            recipient_list=['lalmohit167@gmail.com'],
            fail_silently=False,  # 👈 IMPORTANT
        )

        return redirect('/?success=1')

    return render(request, 'base.html', {
        'projects': projects
    })