from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font("Arial", size=40)
pdf.cell(180, 50, txt="СПРАВКА", ln=1, align="C")
pdf.set_font("Arial", size=15)
pdf.multi_cell(180, 10, txt="Выдана <Имя> <Фамилия>", align='L')
pdf.multi_cell(180, 5, txt="<Текст>", align="L")
pdf.multi_cell(180, 5, txt="М.П.", align="L")

pdf.output("spravka.pdf")
