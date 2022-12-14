from random import *
from tkinter import *

win = Tk()

win.geometry('355x350+600+300')
win.resizable(False, False)
win.title('Password Generator')
def_font = ('Times new roman', 16)
win.config(bg= '#CCC4FF')

answer = StringVar()
d = IntVar()
sym = IntVar()
up = IntVar()
s = IntVar()

def generate_password():
    global answer
    digits = '0123456789'
    symbols = '!@#%^&*()?/><.,'
    res = 'qwertyuiopasdfghjklzxcvbnm'
    ans_lb['state'] = 'normal'
    ans_lb.delete(0, END)
    ans = ''
    len_pass = len_en.get()
    if len_pass == '':
        ans = 'Введите длину пароля'
    else:
        if s.get() == 1:
            digits = digits[2:]
            symbols = '@#%^&*()?/><.,'
            res = 'qwertyupasdfghjkzxcvbnm'
        if d.get() == 1:
            ans += choice(digits)
            res += digits
        if sym.get() == 1:
            ans += choice(symbols)
            res += symbols
        if up.get() == 1:
            ans += choice(res.upper())
            res += res.upper()
        for _ in range(int(len_pass) - (d.get()+sym.get()+up.get())):
            ans += choice(res)

    ans_lb.insert(0, ans)
    ans_lb['state'] = 'readonly'
    return

len_lb = Label(win, text='Длина пароля:', font=def_font, bg= '#CCC4FF')
len_lb.grid(row=0, column=0, sticky='e')

len_en = Entry(win, font=def_font, justify=CENTER, borderwidth=4, width=4)
len_en.grid(row=0, column=1, pady=10, padx=10)

opt1_lb = Label(win, text='Включает цифры', font=def_font, bg= '#CCC4FF', anchor='e')
opt1_lb.grid(row=1, column=0, pady=5, padx=5, sticky='e')

opt2_lb = Label(win, text='Включает символы', font=def_font, bg= '#CCC4FF', anchor='e')
opt2_lb.grid(row=2, column=0, pady=5, padx=5, sticky='e')

opt3_lb = Label(win, text='Включает заглавные буквы', font=def_font, bg= '#CCC4FF', anchor='e')
opt3_lb.grid(row=3, column=0, pady=5, padx=5, sticky='e')

opt4_lb = Label(win, text='Исключает похожие символы', font=def_font, bg= '#CCC4FF', anchor='e')
opt4_lb.grid(row=4, column=0, pady=5, padx=5, sticky='e')

opt1_ch = Checkbutton(win, variable=d, bg= '#CCC4FF', borderwidth=4)
opt1_ch.grid(row=1, column=1, sticky='wesn', )

opt2_ch = Checkbutton(win, variable=sym, bg= '#CCC4FF', borderwidth=4)
opt2_ch.grid(row=2, column=1, sticky='wesn', )

opt3_ch = Checkbutton(win, variable=up, bg= '#CCC4FF', borderwidth=4)
opt3_ch.grid(row=3, column=1, sticky='wesn', )

opt4_ch = Checkbutton(win, variable=s, bg= '#CCC4FF', borderwidth=4)
opt4_ch.grid(row=4, column=1, sticky='wesn', )

gen_bt = Button(win, text='Сгенерировать',font=def_font, command=generate_password, justify=CENTER, borderwidth=4)
gen_bt.grid(row=5, column=0, columnspan=2, sticky='we',  pady=10, padx=10)

ans_lb = Entry(win, font=def_font, state='readonly', justify=CENTER, bg= '#CCC4FF', borderwidth=4)
ans_lb.grid(row=6, column=0, sticky='nswe', columnspan=2, pady=10, padx=10)

win.mainloop()