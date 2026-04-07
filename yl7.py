import tkinter as tk
from datetime import datetime
def main():
    aken = tk.Tk()
    aken.title("isikukoodi validaator")
    aken.geometry("400x200")
    def valideeriTeksti(*args):
        ik = entry_var.get()
        if len(ik) != 11 or not ik.isdigit():
            validation_label.config(text="isikukood peab olema 11 numbrit!", fg="red")
            tulemus_label.config(text="")
            return
        esimene = int(ik[0])
        if esimene % 2 == 0:
            sugu = "naine"
        else:
            sugu = "mees"
        sajand = 0
        if esimene in [1, 2]:
            sajand = 1800
        elif esimene in [3, 4]:
            sajand = 1900
        elif esimene in [5, 6]:
            sajand = 2000
        aasta = sajand + int(ik[1:3])
        kuu = int(ik[3:5])
        paev = int(ik[5:7])
        try:
            synniaeg = datetime(aasta, kuu, paev).strftime("%d.%m.%Y")
            validation_label.config(text="isikukood on korrektne!", fg="green")
            tulemus_label.config(text=f"sugu: {sugu}\nsunniaeg: {synniaeg}")
        except:
            validation_label.config(text="vigane kuupaev!", fg="red")
            tulemus_label.config(text="")
    entry_var = tk.StringVar()
    entry_var.trace_add("write", valideeriTeksti)
    entry = tk.Entry(aken, textvariable=entry_var)
    entry.pack()
    validation_label = tk.Label(aken, text="sisesta isikukood", fg="black")
    validation_label.pack()
    tulemus_label = tk.Label(aken, text="")
    tulemus_label.pack()
    aken.mainloop()
main()