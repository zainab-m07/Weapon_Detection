# # importing modules
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import datetime
import os

def pdf():
    # initializing variables with values
    fileName = 'temp/report.pdf'
    documentTitle = 'sample'
    title = 'Alert!!!'
    subTitle = 'Threat report generated......'
    # Get current date
    current_date = datetime.date.today()

    # Get current time
    current_time = datetime.datetime.now().time()

    # Format date and time
    formatted_date = current_date.strftime("%Y-%m-%d")
    formatted_time = current_time.strftime("%H:%M:%S")
    textLines = [
        'Mumbai',
        formatted_date,
        formatted_time
        ]

    # creating a pdf object
    pdf = canvas.Canvas(fileName, pagesize=letter)

    # setting the title of the document
    pdf.setTitle(documentTitle)

    # registering a external font in python

    # creating the title by setting it's font
    # and putting it on the canvas
    pdf.setFont('Helvetica', 36)
    pdf.drawCentredString(300, 700, title)

    # creating the subtitle by setting it's font,
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 650, subTitle)

    # drawing a line
    pdf.line(30, 640, 550, 640)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 600)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)

    for line in textLines:
        text.textLine(line)

    pdf.drawText(text)

    files_in_temp = os.listdir('temp')

    imgs = []
    img_count = 0
    while img_count < 5:
        imgs.append('temp/'+ files_in_temp[img_count])
        img_count += 1

    img_height = 300
    img_width = 400

    # Set the initial y-coordinate for the top of the page
    y = 500 - img_height

    # Loop through the image paths
    for image in imgs:
        # Check if there's enough space on the current page
        if y < 0 :
            # If not, add a new page
            pdf.showPage()
            y = 800 - (img_height + 20)  # Set the initial y-coordinate for the top of the new page (20 is the gap from top of page)

        # Draw the image
        pdf.drawImage(image, x=100, y=y, width= img_width, height=img_height)

        # Increment the y-coordinate for the next image
        y -= (img_height + 20)  # Adjust this value based on the height of your images and the spacing you want between them

    # Save the PDF
    pdf.save()

    print('pdf generated and saved')
