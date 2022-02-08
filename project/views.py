from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage

def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        file = request.POST.get('file')
         
        data ={
            
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'file': file 
        }
        message = ''' 
        NEw message: {}
        From: {}
        '''.format(data['message'], data['email'])
        email=EmailMessage(data['subject'], message, 'sharique413@gmail.com', ['Sharique413@gmail.com'])
        file = request.FILES['file']
        email.attach(file.name, file.read(), file)
        email.send()
    return render(request, 'contactforms2/index.html', {})