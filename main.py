import tkinter as tk

import write_stock

win = tk.Tk()
win.title("Stock Tracker GUI")

coolFrame = tk.Frame(win)
coolFrame.pack()

tk.Label(coolFrame, text="Choose Currency Pair").pack()

listbox = tk.Listbox(win)
listbox.pack()

currency_pairs = write_stock.get_currency_pairs()
stocks = write_stock.get_stock()

for cp in currency_pairs:
    listbox.insert(tk.END, cp)

for s in stocks:
    listbox.insert(tk.END, s)

def callback():
    write_stock.write_stock_info()

b = tk.Button(win, text="OK", command=callback())

win.mainloop()

