## GENERATES THE REPORTS ##

#importing the modules:

from reportlab.platypus import Image,Table,Paragraph,Flowable,SimpleDocTemplate,Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment,title,paragraph):
    styles = getSampleStyleSheet()
    report_pdf = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    report_description = Paragraph(paragraph, styles['BodyText'])
    report_blank_line = Spacer(1,15)
    report_elements = [report_title,report_description,report_blank_line]
    report_pdf.build(report_elements)