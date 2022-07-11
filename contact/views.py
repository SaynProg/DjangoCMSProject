from django.shortcuts import render, redirect

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.contrib import messages

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = "Ім'я - " + form.cleaned_data['name'] + "\nЕлектронна пошта - " + form.cleaned_data['email_address'] + "\nТема - " + form.cleaned_data['subject'] + '\n\n' + form.cleaned_data['text']
            try:
                send_mail(subject, message, 'u56179410@gmail.com', ['ingognito36708@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Знайдений некоректний заголовок')

            messages.success(request, 'Лист надіслано!')
            return redirect("contact:contact_index")
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})