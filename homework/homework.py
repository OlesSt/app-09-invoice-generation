import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

filepaths = glob.glob("textes/*.txt")

for filepath in filepaths:
    filename = Path(filepath).stem
    title = filename.split(".")[0]
    title = title.title()
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=0, h=16, txt=title, align="L", ln=1)

pdf.output("PDFfromTxt/homework.pdf")
