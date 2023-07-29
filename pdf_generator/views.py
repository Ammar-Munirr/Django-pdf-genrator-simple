from django.shortcuts import render
from django.http import FileResponse
from django.views.generic import TemplateView
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



def pdf_gen(request):
    buff = io.BytesIO()
    c = canvas.Canvas(buff,pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica',12)
    lines = [
        'This is my first line',
        'This is the second one',
        'This one is third'
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buff.seek(0)
    return FileResponse(buff,as_attachment=True,filename='Temp.pdf')


class Home(TemplateView):
    template_name = 'pdf/index.html'