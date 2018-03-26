from tkinter import *
import beckend

def view_all():
    listt=beckend.view()
    list_box.delete(0,END)
    for i in listt:
        list_box.insert(END,i)

def ser():
    listt=beckend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list_box.delete(0,END)
    for i in listt:
        list_box.insert(END,i)

def add():
    beckend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list_box.delete(0,END)
    list_box.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def selected(event):
    ind=list_box.curselection()[0]
    #print(ind)
    global tup
    tup=list_box.get(ind)
    #print(tup)
    entry_title.delete(0,END)
    entry_author.delete(0,END)
    entry_year.delete(0,END)
    entry_isbn.delete(0,END)
    entry_title.insert(END,tup[1])
    entry_author.insert(END,tup[2])
    entry_year.insert(END,tup[3])
    entry_isbn.insert(END,tup[4])

def dele():
    beckend.delete(tup[0])
    view_all()

def upd():
    beckend.update(tup[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_all()



window=Tk()

window.wm_title("Bookstore by Archit")

label_title=Label(window,text="Title")
label_author=Label(window,text="Author")
label_year=Label(window,text="Year")
label_isbn=Label(window,text="ISBN")

label_title.grid(row=0,column=0)
label_author.grid(row=0,column=2)
label_year.grid(row=1,column=0)
label_isbn.grid(row=1,column=2)

title_text=StringVar()
author_text=StringVar()
year_text=StringVar()
isbn_text=StringVar()

entry_title=Entry(window,textvariable=title_text)
entry_author=Entry(window,textvariable=author_text)
entry_year=Entry(window,textvariable=year_text)
entry_isbn=Entry(window,textvariable=isbn_text)

entry_title.grid(row=0,column=1)
entry_author.grid(row=0,column=3)
entry_year.grid(row=1,column=1)
entry_isbn.grid(row=1,column=3)

list_box=Listbox(window,height=6,width=35)
list_box.grid(row=2,column=0,rowspan=6,columnspan=2)

button_view=Button(window,text="View All",width=15,command=view_all)
button_search=Button(window,text="Search Entry",width=15,command=ser)
button_add=Button(window,text="Add Entry",width=15,command=add)
button_update=Button(window,text="Update Selected",width=15,command=upd)
button_delete=Button(window,text="Delete Selected",width=15,command=dele)
button_close=Button(window,text="Close",command=window.destroy,width=15)

button_view.grid(row=2,column=3)
button_search.grid(row=3,column=3)
button_add.grid(row=4,column=3)
button_update.grid(row=5,column=3)
button_delete.grid(row=6,column=3)
button_close.grid(row=7,column=3)

scroll_vertical=Scrollbar(window,orient=VERTICAL)
scroll_vertical.grid(row=2,column=2,rowspan=6)

scroll_horizontal=Scrollbar(window,orient=HORIZONTAL)
scroll_horizontal.grid(row=8,column=0,columnspan=2)

list_box.configure(yscrollcommand=scroll_vertical.set,xscrollcommand=scroll_horizontal.set)
scroll_horizontal.configure(command=list_box.xview)
scroll_vertical.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>',selected)

window.mainloop()
