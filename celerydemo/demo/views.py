from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.shortcuts import redirect
from django.views import generic


from . import tasks, forms


class EmailSendConfirmView(generic.FormView):
    template_name = 'demo/email_confirm_send.html'
    form_class = forms.EmailForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # send email
        try:
            mail.send_mail(
                subject='Prueba django-celery-email',
                message=message,
                recipient_list=(email,),
                from_email=settings.DEFAULT_FROM_EMAIL,
                html_message='<p><strong>Celery</strong> {}</p>'.format(
                    message)
            )
        except Exception:
            messages.error(self.request, 'No se pudo enviar el email')
        else:
            messages.success(self.request, 'El email será enviado')
        return redirect('/')
