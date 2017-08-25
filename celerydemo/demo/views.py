from django.contrib import messages
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
        # import pdb; pdb.set_trace()
        try:
            tasks.send_email.delay(
                to=email,
                subject='Prueba celery',
                txt=message,
                html='<p><strong>Celery</strong> {}</p>'.format(message)
            )
        except tasks.send_email.OperationalError:
            messages.error(self.request, 'No se pudo enviar el email')
        else:
            messages.success(self.request, 'El email será enviado')
        return redirect('/')
