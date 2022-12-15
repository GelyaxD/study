import back_of_tkinter
from tkinter import *
from tkinter import ttk
obj = back_of_tkinter
obj.list1 = []
def clicked():
    obj.add_unit_to_list(list_of_entries[0].get(), list_of_entries[1].get(), list_of_entries[2].get(), list_of_entries[3].get())
    table_insert()
    for i in list_of_entries:
        i.delete(0, 'end')
def clicked_sort_summ():
    obj.sort_list("summ", obj.list1)
    table_insert()

def clicked_sort_price():
    obj.sort_list(" ", obj.list1)
    table_insert()

def table_insert():
    table_refresh()
    for i in obj.list1:
        table.insert("", END, values = (i.getName(), i.getType(), i.getPrice(), i.getKol(), i.getSumm()))
def table_refresh():
    for row in table.get_children():
        table.delete(row)
window = Tk()

window.geometry('1000x400')
window.title("Tkinter base")
columns = ("Имя", "Тип", "Цена", "Колл-во", "Сумма")
table = ttk.Treeview(window, columns = columns, show = "headings")
for i in columns:
    table.heading(i, text = i)
table.heading(2, text = columns[2], command = clicked_sort_price)
table.heading(4, text = columns[4], command = clicked_sort_summ)
table.grid(row = 0, column = 0)
frame1 = Frame(window, width = 1000)
frame1.grid(row = 1, column = 0)
list_of_entries = []
list_of_lables = []
for i in range(len(columns)-1):
    list_of_lables.append(Label(frame1, text = columns[i]))
    list_of_lables[i].grid(row = 0, column = i)
    list_of_entries.append(Entry(frame1, width = 33))
    list_of_entries[i].grid(row = 1, column = i)
list_of_lables[2].bind("<Double-1>", clicked_sort_summ())
btn1 = Button(frame1, text = "Внести значения", command = clicked)
btn1.grid(row = 1, column= 5)
window.mainloop()