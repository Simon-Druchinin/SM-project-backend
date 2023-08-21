import smtplib
from email.message import EmailMessage

from celery import Celery
from src.config import config

celery = Celery("tasks", broker=f"redis://{config.redis.HOST}:{config.redis.PORT}")


def get_email_template_dashboard(username: str) -> EmailMessage:
    email = EmailMessage()
    email['Subject'] = 'Wow! Celery is really cool!'
    email['From'] = config.smtp.USER
    email['To'] = config.smtp.USER
    
    email.set_content(
        '<div>'
        f'<h1 style="color: green">Hi, {username}!</h1>'
        '</div>',
        subtype='html'
    )
    
    return email

@celery.task
def send_email_report(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(config.smtp.HOST, config.smtp.PORT) as smtp_server:
        smtp_server.login(config.smtp.USER, config.smtp.PASSWORD)
        smtp_server.send_message(email)
        