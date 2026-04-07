import tkinter as tk
from PIL import Image, ImageTk

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()

def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open(failinimi)
    pilt = pilt.resize((laius, korgus))
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

def main():
    aken = tk.Tk()
    aken.title("daniel ülesanded")
    aken.geometry("400x600")
    label = tk.Label(aken,
                     text="Daniel Zukov",
                     font=("Arial", 16, "bold"),
                     fg="dark blue",
                     padx=20,
                     pady=10)
    label.pack()
    kuva_pilt(aken, "python_512x512.png", 200, 200)
    
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 12,), fg="black") 
    tekst.pack(expand=True, fill=tk.BOTH)
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.config(yscrollcommand=scrollbar.set)
    failisisu = loe_fail("lorem.txt")
    tekst.insert(tk.INSERT, failisisu)
    aken.mainloop()

if __name__ == "__main__":
    main()