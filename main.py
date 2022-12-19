# Распакуйте и переместите каталог шрифтов в папку fpdf.
# https://github.com/reingart/pyfpdf/releases

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from fpdf import FPDF

window = Tk()

window.geometry('400x245+375+200')
window.resizable(False, False)


def fpdf_processing():
    pdf = FPDF(orientation='P', unit='mm', format='A4')

    pdf.add_page()

    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font("DejaVu", size=40)
    pdf.cell(180, 50, txt="СПРАВКА", ln=1, align="C")
    pdf.set_font("DejaVu", size=15)
    pdf.multi_cell(180, 10, txt="Выдана <Имя> <Фамилия>", align='L')
    pdf.multi_cell(180, 5, txt="<Текст>", align="L")
    pdf.multi_cell(180, 5, txt="М.П.", align="L")

    pdf.output('spravka.pdf')

    notice['text'] = 'Успешно сохранено'


Label(window, text='Имя:').place(x=20, y=10)
Label(window, text='Фамилия:').place(x=20, y=30)
Label(window, text='Текст:').place(x=20, y=50)
Label(window, text='Дата с:').place(x=20, y=130)
Label(window, text='Дата по:').place(x=20, y=150)

name = Text(window, height=1, width=20)
surname = Text(window, height=1, width=20)
text = ScrolledText(window, height=4, width=30)
date_from = Text(window, height=1, width=20)
date_till = Text(window, height=1, width=20)
button = Button(window, text='Сохранить PDF', width=20, command=fpdf_processing, bg='red', fg='white')
notice = Label(window, text='')

name.place(x=90, y=10)
surname.place(x=90, y=30)
text.place(x=90, y=55)
date_from.place(x=90, y=130)
date_till.place(x=90, y=150)
button.place(x=130, y=185)
notice.place(x=145, y=215)

window.mainloop()
