# Распакуйте и переместите каталог шрифтов в папку fpdf.
# https://github.com/reingart/pyfpdf/releases

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from fpdf import FPDF

window = Tk()

window.geometry('400x220+375+200')
window.resizable(False, False)


def fpdf_processing():
    pdf = FPDF(orientation='P', unit='mm', format='A4')

    pdf.add_page()

    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    # pdf.set_font("Arial", size=40)
    pdf.cell(180, 50, txt="СПРАВКА", ln=1, align="C")
    # pdf.set_font("Arial", size=15)
    pdf.multi_cell(180, 10, txt="Выдана <Имя> <Фамилия>", align='L')
    pdf.multi_cell(180, 5, txt="<Текст>", align="L")
    pdf.multi_cell(180, 5, txt="М.П.", align="L")

    pdf.output('spravka.pdf')


Label(window, text='Имя:').place(x=20, y=10)
Label(window, text='Фамилия:').place(x=20, y=30)
Label(window, text='Текст:').place(x=20, y=50)
Label(window, text='Дата с:').place(x=20, y=130)
Label(window, text='Дата по:').place(x=20, y=150)

name = Text(window, height=1, width=20)
title = Text(window, height=1, width=20)
main_text = ScrolledText(window, height=4, width=30)
data = Text(window, height=1, width=20)
creator_name = Text(window, height=1, width=20)

name.place(x=90, y=10)
title.place(x=90, y=30)
main_text.place(x=90, y=55)
data.place(x=90, y=130)
creator_name.place(x=90, y=150)

Button(window, text='Сохранить PDF', width=20, command=fpdf_processing, bg='red', fg='white').place(x=130, y=185)

window.mainloop()
