# Распакуйте и переместите каталог шрифтов в папку fpdf.
# https://github.com/reingart/pyfpdf/releases

from tkinter import *
from datetime import datetime
from fpdf import FPDF

window = Tk()

window.geometry('380x200+375+200')
window.resizable(False, False)


def fpdf_processing():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    text_name = name.get('1.0', 'end-1c')
    text_surname = surname.get('1.0', 'end-1c')
    text_date_from = date_from.get('1.0', 'end-1c')
    text_date_till = date_till.get('1.0', 'end-1c')

    text = f"{text_name} {text_surname} болел с {text_date_from} по {text_date_till} ангиной."

    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font("DejaVu", size=40)
    pdf.cell(0, 50, txt="СПРАВКА", ln=1, align="C")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(0, 10, txt=text, align='L', ln=1)
    pdf.cell(0, 10, txt='', align='L', ln=1)
    pdf.cell(0, 10, txt='', align='L', ln=1)
    pdf.cell(0, 10, txt=str(datetime.now().strftime("%d.%m.%Y")) + ' г. ' + '_' * 25, align="R", ln=1)
    pdf.image("./stamp.png", x=20, y=80, w=40, h=40, type='PNG')

    pdf.output('spravka.pdf')

    notice['text'] = 'Успешно сохранено'


Label(window, text='Имя:').place(x=20, y=10)
Label(window, text='Фамилия:').place(x=20, y=40)
Label(window, text='Дата с:').place(x=20, y=70)
Label(window, text='Дата по:').place(x=20, y=100)

name = Text(window, height=1, width=30)
surname = Text(window, height=1, width=30)
date_from = Text(window, height=1, width=30)
date_till = Text(window, height=1, width=30)
button = Button(window, text='Сохранить PDF', width=20, command=fpdf_processing, bg='red', fg='white')
notice = Label(window, text='')

name.place(x=90, y=10)
name.focus_set()
surname.place(x=90, y=40)
date_from.place(x=90, y=70)
date_till.place(x=90, y=100)
button.place(x=130, y=140)
notice.place(x=145, y=170)

window.mainloop()
