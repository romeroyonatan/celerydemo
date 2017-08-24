import logging
import time

from django.conf import settings
from django.core.mail import send_mail

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def send_email(to, subject, txt, html):
    logger.info('Sending mail to: %r subject: %r', to, subject)
    time.sleep(5)
    send_mail(
        subject=subject,
        message=txt,
        recipient_list=(to,),
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html,
    )
    return 'Email to %r sent successfully' % to
