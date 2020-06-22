import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

import read_stock
import write_stock

win = tk.Tk()
win.title("Stock Tracker GUI")

coolFrame = tk.Frame(win)
coolFrame.pack()

tk.Label(coolFrame, text="Choose Currency Pair").pack()

listbox = tk.Listbox(win, width=30, height=15, selectmode=tk.EXTENDED)
listbox.pack()

currency_pairs = write_stock.get_currency_pairs()
stocks = write_stock.get_stock()

for cp in currency_pairs:
    listbox.insert(tk.END, cp)

for s in stocks:
    listbox.insert(tk.END, s)


def callback():
    selected_stock_name = listbox.get(listbox.curselection())

    if listbox.get(listbox.curselection()):
        stock_info = write_stock.write_stock_info(listbox.get(listbox.curselection()))
        result = messagebox.askyesno("Complete!", "Do you wish to save " + selected_stock_name + ".csv ?")

        if result:
            save(stock_info, selected_stock_name)


def save(stock_info, selected_stock_name):
    contents = stock_info
    new_file = asksaveasfile(parent=win, initialfile=selected_stock_name+".csv",
                             title="Save file", defaultextension=".csv",
                             filetypes=(("Comma-seperated Values (CSV) file", "*.csv"),))

    if new_file:
        new_file.write(str(contents))
        new_file.close()

b = tk.Button(win, text="OK", command=callback)
b.pack()

win.mainloop()
