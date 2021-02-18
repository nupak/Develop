from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from scientistSite.settings import SITE_NAME, EMAIL_HOST_USER


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = SITE_NAME+"{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    hello_text = "Вы запросили сброс пароля от личного кабинета. " \
                 "Для изменения пароля перейдите по ссылке:"


    send_mail(
        # title:
        "Cброс пароля от личного кабинета на сайте {title}".format(title=SITE_NAME[8:]),
        # message:
        (hello_text+email_plaintext_message),
        # from:
        EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )