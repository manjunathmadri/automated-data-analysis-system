from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from datetime import datetime
import os

def generate_pdf(report_data):
    os.makedirs("outputs", exist_ok=True)

    file_path = "outputs/report.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # ---------------- TITLE ----------------
    elements.append(Paragraph("<b>Automated Data Analysis Report</b>", styles["Title"]))
    elements.append(Spacer(1, 10))

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elements.append(Paragraph(f"Generated on: {current_time}", styles["Normal"]))
    elements.append(Spacer(1, 20))

    # ---------------- TABLE ----------------
    data = [["Metric", "Value"]]
    for key, value in report_data.items():
        data.append([key, str(value)])

    table = Table(data, colWidths=[3 * inch, 2 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.grey),
        ('ALIGN', (1,1), (-1,-1), 'CENTER')
    ]))

    elements.append(table)
    elements.append(Spacer(1, 40))

    # ---------------- BAR CHART ----------------
    drawing = Drawing(400, 200)
    chart = VerticalBarChart()
    chart.x = 50
    chart.y = 30
    chart.height = 125
    chart.width = 300

    values = [float(v) for v in report_data.values()]
    chart.data = [values]
    chart.categoryAxis.categoryNames = list(report_data.keys())

    chart.barWidth = 25
    chart.barSpacing = 15
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = max(values) * 1.2

    drawing.add(chart)
    elements.append(drawing)

    # ---------------- SECOND PAGE ----------------
    elements.append(PageBreak())
    elements.append(Paragraph("<b>Summary & Distribution</b>", styles["Heading1"]))
    elements.append(Spacer(1, 30))

    # ---------------- PIE CHART ----------------
    pie_drawing = Drawing(400, 250)
    pie = Pie()
    pie.x = 150
    pie.y = 15
    pie.width = 200
    pie.height = 200
    pie.data = values
    pie.labels = list(report_data.keys())

    pie_drawing.add(pie)
    elements.append(pie_drawing)

    elements.append(Spacer(1, 40))
    elements.append(Paragraph("Confidential - Automated Data Analysis System", styles["Italic"]))

    doc.build(elements)
    return file_path