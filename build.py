from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                Flowable, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT
import os

file_path = "./Thomas_Wollin_Resume_Enhanced_v3.pdf"

doc = SimpleDocTemplate(file_path, pagesize=letter,
                        rightMargin=40, leftMargin=40,
                        topMargin=40, bottomMargin=40)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='HeaderName', fontSize=22, leading=26, spaceAfter=10, alignment=TA_LEFT))
styles.add(ParagraphStyle(name='SectionHeader', fontSize=14, leading=18, spaceBefore=12, spaceAfter=4, textColor=colors.HexColor("#d40000")))

elements = []

header_parts = '<b>THOMAS</b> <font color="#d40000"><b>WOLLIN</b></font>'
elements.append(Paragraph(header_parts, styles['HeaderName']))

contact_text = 'Barrie, ON L4N 7L6  |  289-338-6990  |  Thomwollin@gmail.com'

class BlackBar(Flowable):
    def __init__(self, width, height, text):
        super().__init__()
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        self.canv.setFillColor(colors.black)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)
        self.canv.setFillColor(colors.white)
        self.canv.setFont("Helvetica", 10)
        text_y = (self.height - 10) / 2 + 2
        self.canv.drawCentredString(self.width/2, text_y, self.text)

elements.append(BlackBar(500, 22, contact_text))
elements.append(Spacer(1, 10))

def add_section_header(title):
    elements.append(Paragraph(title, styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#d40000")))
    elements.append(Spacer(1, 4))

add_section_header("Professional Summary")
summary_text = ("Team Leader turned emerging full-stack web developer with 7+ years of leadership experience in fast-paced customer-service environments and recent completion of the University of Toronto School of Continuing Learning Full-Stack Web Development Bootcamp. "
                "Combines proven people-management and problem-solving expertise with strong technical proficiency in HTML5, CSS3, JavaScript (ES6+), React, Node.js, Express, SQL/MySQL, MongoDB, and Git. "
                "Adept at designing responsive user interfaces, building RESTful APIs, and delivering real-time, data-driven solutions. "
                "Recognized for analytical thinking, attention to detail, and the ability to translate complex requirements into practical outcomes that drive customer satisfaction and business results.")
elements.append(Paragraph(summary_text, styles['BodyText']))

add_section_header("Skills")
skills_col1 = ["De-Escalating Conflicts", "Excellent Listening Skills", "Effective Customer Service",
               "Leading Employees", "People Management", "Verbal and Written Communications"]
skills_col2 = ["SOP Adherence", "Analytical Thinking", "Attention to Detail",
               "Teamwork and Collaboration", "Coaching and Mentoring"]

data = [[Paragraph('<br/>'.join(skills_col1), styles['BodyText']),
         Paragraph('<br/>'.join(skills_col2), styles['BodyText'])]]
skills_table = Table(data, colWidths=[250, 250])
elements.append(skills_table)

add_section_header("Technical Proficiencies")
tech_text = ("<b>Foundational Web Technologies:</b> HTML5, CSS3, JavaScript (ES6+)<br/>"
             "<b>Front-End Libraries & Frameworks:</b> React, Bootstrap, Bulma, Materialize, Handlebars<br/>"
             "<b>Server-Side Development:</b> Node.js, Express, RESTful API design<br/>"
             "<b>Real-Time Communication:</b> Socket.io<br/>"
             "<b>Databases:</b> SQL & MySQL, NoSQL & MongoDB<br/>"
             "<b>Version Control & Collaboration:</b> Git & GitHub<br/>"
             "<b>Additional Tools:</b> Responsive design techniques, Agile workflows, VS Code, Linux & CLI basics")
elements.append(Paragraph(tech_text, styles['BodyText']))

add_section_header("Work History")

def job_entry(title, company, location, date, bullets):
    header = f"<b>{title}</b>  |  {company} - {location}  <i>{date}</i>"
    elements.append(Paragraph(header, styles['BodyText']))
    for b in bullets:
        elements.append(Paragraph(b, styles['BodyText'], bulletText="•"))
    elements.append(Spacer(1, 6))

# First job stays on first page
job_entry("Team Leader", "HGS Canada", "Barrie, ON", "05/2018 - 04/2024", [
    "Coordinated with local law enforcement regarding potential identity-theft and credit-card-fraud cases, ensuring accurate documentation and customer protection.",
    "Dispatched appropriate technicians and equipment to resolve client concerns, reducing average resolution time by 15%.",
    "Provided over-the-phone support for TV, Internet, Home Phone, email, and communications issues across multiple platforms and devices.",
    "Excelled in sales-based commissions program, increasing yearly income 20%.",
    "Headed the Billing Department Escalations Team and resolved highest level escalations for client using excellent listening skills.",
    "Managed between 15-20 team members and helped inspire my team to improve key performance indicators themselves."
])

# Page break before Transcom job
elements.append(PageBreak())

job_entry("Team Leader", "Transcom Worldwide", "Barrie, ON", "01/2014 - 01/2018", [
    "Mentored and guided employees to foster proper completion of assigned duties.",
    "Built strong relationships with customers through positive attitude and attentive response.",
    "Established open and professional relationships with team members to achieve quick resolutions."
])

job_entry("Water Spider", "Flextronics", "Newmarket, ON", "01/2013 - 01/2014", [
    "Managed raw materials for a solar-panel production line, ensuring continuous supply and meeting strict production quotas on 12-hour shifts.",
    "Maintained a clean and organized back area, demonstrating strong time-management and safety practices."
])

job_entry("Assistant Manager", "Georgina Garden Center", "Keswick, ON", "01/2011 - 01/2013", [
    "Advised customers on plant care, lighting, and fertilization, driving repeat business and positive word-of-mouth.",
    "Developed and maintained fertilizing and watering schedules, monitoring soil pH and nutrient concentrations for optimal plant health.",
    "Operated heavy machinery (Bobcat) for deliveries, ensuring safe and efficient loading."
])

add_section_header("Education")
education_text = ("<b>Certificate, Full-Stack Web Development (Part-Time)</b> – University of Toronto School of Continuing Learning, Toronto, ON (2025)<br/>"
                  "<b>Game Development – Computer Science (Coursework)</b> – Algonquin College, Ottawa, ON (2012-2013)<br/>"
                  "<b>High School Diploma</b> – Keswick High School, Keswick, ON (2011)")
elements.append(Paragraph(education_text, styles['BodyText']))

add_section_header("Certifications")
cert_text = ("Standard First Aid & CPR<br/>"
             "Full-Stack Web Development Certificate – University of Toronto School of Continuing Studies (2025)")
elements.append(Paragraph(cert_text, styles['BodyText']))

doc.build(elements)
file_path
