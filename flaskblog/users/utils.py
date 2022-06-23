import os
import secrets
import smtplib
import ssl
from email.message import EmailMessage
from PIL import Image
from flask import url_for, current_app
from flask_login import current_user



def save_picture(form_picture):
    if f'{current_user.image_file}' != 'default.jpg':
        os.remove(f'flaskblog/static/profile_pics/{current_user.image_file}')
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    logout_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(logout_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    # token = user.get_reset_token()
    email_sender = 'bsjk.technical@gmail.com'
    email_password = 'qcirimmsngfkscho'
    email_receiver = [user.email]
    subject = 'Password Reset Request'

    body = f"""To reset your password, visit the following link:
    http://127.0.0.1:5000/reset_token
    {url_for('main.home')}
    If you did not make this request then simply ignore this email and no changes will be made.
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


    # account: bsjk.technical@gmail.com
    # password: ibs.tech.admin
    # app_password: ibs.technical
    # app_passwords_16: qcirimmsngfkscho