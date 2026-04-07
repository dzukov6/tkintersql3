import tkinter as tk
from tkinter import messagebox

def main():
    aken = tk.Tk()
    aken.title("Laenukalkulaator")
    aken.geometry("400x350")

    def arvuta_makse():
        laenusumma_text = entry_laenusumma.get()
        intress_text = entry_intress.get()
        periood_text = entry_periood.get()

        if not laenusumma_text or not intress_text or not periood_text:
            messagebox.showerror("Viga", "Koik valjad peavad olema taidetud.")
            return

        try:
            laenusumma = float(laenusumma_text)
            aastane_intress = float(intress_text)
            aastad = int(periood_text)

            kuuintress = aastane_intress / 12 / 100
            maksete_arv = aastad * 12
            igakuine_makse = laenusumma * kuuintress / (1 - (1 + kuuintress) ** -maksete_arv)

            label_vastus.config(text=f"Igakuine makse: {igakuine_makse:.2f} €", fg="black")
        except ValueError:
            messagebox.showerror("Viga", "Sisesta korrektne number.")

    tk.Label(aken, text="Laenusumma (€):").pack(pady=(10, 0))
    entry_laenusumma = tk.Entry(aken)
    entry_laenusumma.pack(pady=5)

    tk.Label(aken, text="Aastane intressimaar (%):").pack(pady=(10, 0))
    entry_intress = tk.Entry(aken)
    entry_intress.pack(pady=5)

    tk.Label(aken, text="Laenuperiood (aastates):").pack(pady=(10, 0))
    entry_periood = tk.Entry(aken)
    entry_periood.pack(pady=5)

    nupp = tk.Button(aken, text="Arvuta", command=arvuta_makse)
    nupp.pack(pady=20)

    label_vastus = tk.Label(aken, text="", font=("Arial", 12))
    label_vastus.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()