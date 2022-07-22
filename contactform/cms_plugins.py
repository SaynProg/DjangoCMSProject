from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

@plugin_pool.register_plugin
class ContactPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Контакта Форма")
    render_template = "contactform/contactform.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = "Ім'я - " + form.cleaned_data['name'] + "\nЕлектронна пошта - " + form.cleaned_data['email_address'] + "\nТема - " + form.cleaned_data['subject'] + '\n\n' + form.cleaned_data['text']
                # try:
                send_mail(subject, message, 'u56179410@gmail.com', ['ingognito36708@gmail.com'])
                # except BadHeaderError:
                #     return HttpResponse('Знайдений некоректний заголовок')

            messages.success(request, 'Лист надіслано!')

        context.update( {
            'instance': instance,
            'placeholder': placeholder,
            'form': ContactForm(),
            })

        form = ContactForm()
        return context