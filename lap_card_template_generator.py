# Author : Sunil Jayaprakash
# E-mail : sunil.jayaprakash@gmail.com
from calendar import monthcalendar, month_name
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def lap_card_template_generator():
    now = datetime.now()
    month = now.month
    year = now.year
    calendar = monthcalendar(year, month)
    month_label = month_name[month]

    # Create a PDF
    c = canvas.Canvas("lap_card_template.pdf", pagesize=letter)
    width, height = letter

    # Margins
    margin_top = 11
    margin_bottom = 10
    margin_left = 50
    margin_right = 10

    # Box dimensions
    box_width = 245
    box_height = 250
    gap = 10

    # Calculate number of boxes that fit horizontally and vertically
    num_boxes_x = int((width - margin_left - margin_right + gap) // (box_width + gap))
    num_boxes_y = int((height - margin_top - margin_bottom + gap) // (box_height + gap))

    for row in range(num_boxes_y):
        for col in range(num_boxes_x):
            box_x = margin_left + col * (box_width + gap)
            box_y = height - margin_top - (row + 1) * (box_height + gap) + gap

            # Draw a box outline
            c.setStrokeColor(colors.black)
            c.setLineWidth(2)
            c.rect(box_x, box_y, box_width, box_height)

            # Title
            c.setFont("Helvetica-Bold", 16)
            c.drawString(box_x + 20, box_y + box_height - 30, "Lap Card")

            # Placeholder for Kid's Name
            c.setFont("Helvetica", 12)
            c.drawString(box_x + 20, box_y + box_height - 60, "Kid's Name: ____________________")

            # Placeholder for Activity
            c.drawString(box_x + 20, box_y + box_height - 80, "Activity  : ______________________")

            # Draw table
            table_x = box_x + 20
            table_y = box_y + box_height - 100
            cell_width = 30
            cell_height = 20
            c.setLineWidth(0.5)

            # Draw rows
            for i in range(8):
                c.line(table_x, table_y - i * cell_height, table_x + 7 * cell_width, table_y - i * cell_height)

            # Draw columns
            for i in range(8):
                c.line(table_x + i * cell_width, table_y, table_x + i * cell_width, table_y - 7 * cell_height)

            # Fill in the calendar
            days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
            for i, day in enumerate(days):
                c.drawString(table_x + i * cell_width + 5, table_y - cell_height + 5, day)


    # Save the PDF
    c.save()

# Generate the template
lap_card_template_generator()