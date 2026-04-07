import tkinter as tk

aken = tk.Tk()
aken.title("pitsa tellimisvorm")
aken.geometry("300x600")
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
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
silt = tk.Label(aken, text="vali suurus hind")
silt.pack(pady=5)
checkbox1 = tk.Checkbutton(aken, text="vaike 5 eur", variable=var1)
checkbox1.pack()
checkbox2 = tk.Checkbutton(aken, text="suur 8 eur", variable=var2)
checkbox2.pack()
checkbox3 = tk.Checkbutton(aken, text="pere 12 eur", variable=var3)
checkbox3.pack()
silt2 = tk.Label(aken, text="vali lisandid hind")
silt2.pack(pady=5)
checkbox4 = tk.Checkbutton(aken, text="juust 1 eur", variable=var4)
checkbox4.pack()
checkbox5 = tk.Checkbutton(aken, text="pepperoni 1.5 eur", variable=var5)
checkbox5.pack()
checkbox6 = tk.Checkbutton(aken, text="seen 1 eur", variable=var6)
checkbox6.pack()
silt3 = tk.Label(aken, text="vali kuller hind")
silt3.pack(pady=5)
btn_kuller = tk.Button(aken, text="kuller 3 eu)", command=arvuta_kuller_summa)
btn_kuller.pack(pady=10)
btn_arvuta = tk.Button(aken, text="arvuta summa", command=uue_akna_avamine(arvuta_summa()))
btn_arvuta.pack(pady=10)
aken.mainloop()