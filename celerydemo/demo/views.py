from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic


from . import tasks


class EmailSendConfirmView(generic.TemplateView):
    template_name = 'demo/email_confirm_send.html'

    def post(self, request, *args, **kwargs):
        # send email
        tasks.send_email.delay(
            to='arba@mailinator.com',
            subject='Prueba celery',
            txt='Todo salio bien',
            html='<p><strong>Celery</strong> funciona!</p>'
        )
        messages.success(request, 'Email enviado')
        return redirect('/')
