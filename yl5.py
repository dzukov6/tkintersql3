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

    frame_laenusumma = tk.Frame(aken)
    frame_laenusumma.pack(pady=5, padx=10, anchor='w')
    tk.Label(frame_laenusumma, text="Laenusumma (€):").pack(side='left')
    entry_laenusumma = tk.Entry(frame_laenusumma)
    entry_laenusumma.pack(side='left')

    frame_intress = tk.Frame(aken)
    frame_intress.pack(pady=5, padx=10, anchor='w')
    tk.Label(frame_intress, text="Aastane intressimaar (%):").pack(side='left')
    entry_intress = tk.Entry(frame_intress)
    entry_intress.pack(side='left')

    frame_periood = tk.Frame(aken)
    frame_periood.pack(pady=5, padx=10, anchor='w')
    tk.Label(frame_periood, text="Laenuperiood (aastates):").pack(side='left')
    entry_periood = tk.Entry(frame_periood)
    entry_periood.pack(side='left')

    nupp = tk.Button(aken, text="Arvuta", command=arvuta_makse)
    nupp.pack(pady=20)

    label_vastus = tk.Label(aken, text="", font=("Arial", 12))
    label_vastus.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()