from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from django.views.generic import TemplateView
from django.http import FileResponse
import io

def pdf_gen(request):
    buff = io.BytesIO()
    c = canvas.Canvas(buff, pagesize=letter, bottomup=0)

    # Set the width of the text box
    text_width = 6.5 * inch

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 24)
    textob.textLine('Agreement With User !!')
    c.drawText(textob)

    textob.setFont('Helvetica', 12)
    textsfile = "/home/able/Desktop/django_pdf/textfile/demo.txt" #change it path according to your configurations :) It's just an example as we can also write text from text file.
    file = open(textsfile, 'r')
    lines = file.readlines()

    for line in lines:
        words = line.strip().split()
        wrapped_line = ""

        for word in words:
            current_line_width = c.stringWidth(wrapped_line, 'Helvetica', 12)
            word_width = c.stringWidth(word, 'Helvetica', 12)
            if current_line_width + word_width < text_width:
                wrapped_line += word + " "
            else:
                textob.textLine(wrapped_line.strip())
                wrapped_line = word + " "
        textob.textLine(wrapped_line.strip())

    c.drawText(textob)
    c.showPage()
    c.save()
    buff.seek(0)
    return FileResponse(buff, as_attachment=True, filename='Temp.pdf')



class Home(TemplateView):
    template_name = 'pdf/index.html'