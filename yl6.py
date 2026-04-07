import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def main():
    aken = tk.Tk()
    aken.title("profiili sisestamine")
    aken.geometry("500x250")

    def salvesta():
        messagebox.showinfo("salvestatud", "profiil salvestatud.")
    img = Image.open("python_512x512.png")     
    img = img.resize((120, 120))                
    pilt = ImageTk.PhotoImage(img)              
    pilt_label = tk.Label(aken, image=pilt)
    pilt_label.image = pilt                      
    pilt_label.grid(row=0, column=0, rowspan=5, padx=5, pady=5, sticky="nsew")
    tk.Label(aken, text="nimi:").grid(row=0, column=1, sticky='e', padx=5, pady=5)
    entry_nimi = tk.Entry(aken)
    entry_nimi.grid(row=0, column=2, columnspan=3, sticky='we', padx=5, pady=5)
    tk.Label(aken, text="silmade värv:").grid(row=1, column=1, sticky='e', padx=5, pady=5)
    entry_silmade_varv = tk.Entry(aken)
    entry_silmade_varv.grid(row=1, column=2, columnspan=3, sticky='we', padx=5, pady=5)
    tk.Label(aken, text="pikkus:").grid(row=2, column=1, sticky='e', padx=5, pady=5)
    entry_pikkus = tk.Entry(aken)
    entry_pikkus.grid(row=2, column=2, sticky='we', padx=5, pady=5)
    tk.Label(aken, text="cm").grid(row=2, column=3, sticky='w', padx=5)
    tk.Label(aken, text="kaal:").grid(row=3, column=1, sticky='e', padx=5, pady=5)
    entry_kaal = tk.Entry(aken)
    entry_kaal.grid(row=3, column=2, sticky='we', padx=5, pady=5)
    tk.Label(aken, text="kg").grid(row=3, column=3, sticky='w', padx=5)

    tk.Button(aken, text="salvesta", command=salvesta).grid(row=5, column=0, columnspan=5, pady=10)

    for i in range(5):
        aken.columnconfigure(i, weight=1)
    for i in range(6):
        aken.rowconfigure(i, weight=1)

    aken.mainloop()

if __name__ == "__main__":
    main()