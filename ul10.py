import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

aken = ttk.Window(themename="darkly")
aken.title("pitsa tellimisvorm")
aken.geometry("300x600")
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.StringVar(value="Ei")
def arvuta_summa():
    summa = 0
    if var1.get() == 1:
        summa += 5
    if var2.get() == 1:
        summa += 8
    if var3.get() == 1:
        summa += 12
    
    if var4.get() == 1:
        summa += 1
    if var5.get() == 1:
        summa += 1.5
    if var6.get() == 1:
        summa += 1
    
    return summa
def arvuta_kuller_summa():
    summa = arvuta_summa()
    if var7.get() == 1:
        summa += 3
    
    uue_akna_avamine(summa)
def uue_akna_avamine(summa):
    new_window = tk.Toplevel()
    new_window.title("pitsa hind")
    new_window.geometry("200x100")
    tk.Label(new_window, text=f"pitsa hind on: {summa} eur").pack()
    tk.Button(new_window, text="sulge aken", command=new_window.destroy).pack()

id2 = tk.Label(aken, text="kasutaja ID:")
id2.pack(pady=5)
id1 = ttk.Entry(aken)
id1.pack(pady=5)
silt = tk.Label(aken, text="vali suurus hind")
silt.pack(pady=5)
checkbox = ttk.Frame(aken)
checkbox.pack(pady=10)
checkbox1 = ttk.Radiobutton(checkbox, text="vaike 5 eur", bootstyle="primary",  variable=var1)
checkbox1.pack(anchor="w")
checkbox2 = ttk.Radiobutton(checkbox, text="suur 8 eur", bootstyle="primary", variable=var2)
checkbox2.pack(anchor="w")
checkbox3 = ttk.Radiobutton(checkbox, text="pere 12 eur", bootstyle="primary", variable=var3)
checkbox3.pack(anchor="w")

silt2 = tk.Label(aken, text="vali lisandid hind")
silt2.pack(pady=5)

checkbox_frame = ttk.Frame(aken)
checkbox_frame.pack(pady=10)
checkbox1 = ttk.Checkbutton(checkbox_frame, text="juust 1 eur", variable=var4)
checkbox1.pack(anchor="w")
checkbox2 = ttk.Checkbutton(checkbox_frame, text="pepperoni 1.5 eur", variable=var5)
checkbox2.pack(anchor="w")
checkbox3 = ttk.Checkbutton(checkbox_frame, text="seen 1 eur", variable=var6)
checkbox3.pack(anchor="w")

silt3 = tk.Label(aken, text="vali kuller hind")
silt3.pack(pady=5)

label = tk.Label(aken, text="vali kattetoimetamine (hind):")
label.pack(pady=5)
arvuta = ["Ei", "Jah"]
btn_arvuta = ttk.Combobox(aken, values=arvuta, textvariable=var7)
btn_arvuta.pack(pady=5)

arv34 = ttk.Button(aken, text="Arvuta hind", bootstyle="success", command=arvuta_kuller_summa)
arv34.pack(pady=20)
aken.mainloop()