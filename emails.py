import email.message
import os
import mimetypes
import smtplib

def generate_email(sender,receiver,subject,body,attachment=None):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    if attachment:
        attachment_path = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split("/",1)

        with open(attachment, "rb") as attach:
            message.add_attachment(attach.read(), maintype=mime_type,subtype=mime_subtype,filename=attachment_path)

    return message


def send_email(message):
    server = smtplib.SMTP("localhost")
    server.send_message(message)
    server.quit()

