"""A intenção do código é criar um arquivo PDF com base em um arquivo csv, para isso
foram criadas as tabelas abaixo. Os for loops vão iterar pelas colunas das tabelas para criar
os títulos (header) com base na tabela de nome topic, o for loop aninhado (nested) vai criar linhas
com base no pdf.line e o outro for loop vai criar um número de páginas para cada header de acordo
com a coluna pages. O resto do código são as configurações de distância, preenchimento (padding) e
estilo de letra de acordo com a bibliotexa fpdf"""

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
         ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")