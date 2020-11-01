from tkinter import *
from tkinter.ttk import Combobox
import count
import GetData


def click_button():
    time = time_entry.get()
    l_time = time.split(':')
    hour = int(l_time[0])+1##################
    interval = int(interval_entry.get())####################
    rout_num = variable.get()#######################
    bus_num = count.bus_manage(interval, rout_num, hour)
    res_label = Label(text="Необходимое количество автобусов на маршруте: " + str(int(bus_num[0])) + '(малой вместимости), ' + str(int(bus_num[1])) + '(большой вместимости)')
    res_label.place(relx=.5, rely=.5, anchor="c")

count.config_sys()
root = Tk()
root.title("Графическая программа на Python")
root.geometry('800x600')

time_label = Label(text="Введите текущее время:")
time_label.place(relx=.25, rely=.2, anchor="c")
time_entry = Entry()
time_entry.place(relx=.25, rely=.3, anchor="c")

interval_label = Label(text="Введите интервал в минутах:")
interval_label.place(relx=.5, rely=.2, anchor="c")
interval_entry = Entry()
interval_entry.place(relx=.5, rely=.3, anchor="c")

rout_label = Label(text="Выберите маршрут:")
rout_label.place(relx=.75, rely=.2, anchor="c")
variable = StringVar(root)
list_opt = []
rout_dict = count.rout_dict
for r_num in rout_dict:
    list_opt.append(rout_dict[r_num])
variable.set(list_opt[0])
var_list = Combobox(root, textvariable=variable, values=list_opt)
var_list.place(relx=.75, rely=.3, anchor="c")

btn = Button(text="Сделать хорошо",          # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             command=click_button
             )
btn.place(relx=.5, rely=.7, anchor="c")

root.mainloop()