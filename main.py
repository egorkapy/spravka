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
    pdf.cell(0, 50, txt="СПРАВКА", ln=1, align="C")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(0, 10, txt=f"Выдана {name.get('1.0', 'end-1c')} {surname.get('1.0', 'end-1c')}", align='L', ln=1)
    pdf.multi_cell(0, 10, txt=text.get('1.0', 'end-1c'), align="L")
    pdf.cell(0, 10, txt="Врач" + '_' * 30, align="R", ln=1)
    pdf.cell(0, 15, txt=f"C {date_from.get('1.0', 'end-1c')} по {date_till.get('1.0', 'end-1c')}", align="R", ln=1)
    pdf.cell(0, 25, txt="М.П.", align="L", ln=1)
    pdf.image("./stamp.png", x=20, y=100, w=50, h=50, type='PNG')

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
name.focus_set()
surname.place(x=90, y=30)
text.place(x=90, y=55)
date_from.place(x=90, y=130)
date_till.place(x=90, y=150)
button.place(x=130, y=185)
notice.place(x=145, y=215)

window.mainloop()
