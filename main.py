from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import random
 
def create_addition_worksheet(input_digits, output_filename='addition_worksheet.pdf'):
    # Define the size of the PDF
    width, height = A4
    margin = 50
    line_height = 20
    problem_spacing = 40
 
    # Convert input digits to a list of integers
    digits = list(map(int, input_digits.split()))
 
    # Create a canvas to draw on
    c = canvas.Canvas(output_filename, pagesize=A4)
 
    # Set the title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2.0, height - margin, "Addition Worksheet")
 
    # Set the starting position for the first problem
    y = height - margin - 60
 
    # Set the font for the problems
    c.setFont("Helvetica", 14)
 
    # Generate problems
    for i in range(1, 21):  # Generate 20 problems
        num1 = random.choice(digits)
        num2 = random.choice(digits)
        problem = f"{num1} + {num2} = "
        c.drawString(margin, y, problem)
        y -= problem_spacing
 
        # Check if we need to start a new column
        if y < margin:
            y = height - margin - 60
            margin += 200
            if margin > width - 150:  # If margin exceeds page width, start a new page
                margin = 50
                c.showPage()
                c.setFont("Helvetica", 14)
    # Save the PDF
    c.save()
