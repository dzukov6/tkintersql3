import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from pathlib import Path
def valige_failid():
    failid = filedialog.askopenfilenames(
        filetypes=(("jpg ja jpeg failid", "*.jpg;*.jpeg"), ("koik failid", "*.*")),
        title="vali pildid"
    )
    if failid:
        unikaalsed_failid = list(set(failid))  
        failide_nimed.set("\n".join(unikaalsed_failid))
    else:
        messagebox.showinfo("teade", "uhtegi faili ei valitud.")
def salvestage_pildid():
    kaust = filedialog.askdirectory(title="vali kaust salvestamiseks")
    if kaust:
        failid = failide_nimed.get().split("\n")
        if not failid or failid == ['']:
            messagebox.showerror("viga", "palun valige pildid.")
            return
        for fail in failid:
            if fail:
                try:
                    pilt = Image.open(fail)
                    pilt = pilt.resize((200, 200))
                    salvestamise_path = Path(kaust) / Path(fail).name
                    pilt.save(salvestamise_path)
                except Exception as e:
                    messagebox.showerror("viga", f"viga pildi tootlemisel: {str(e)}")
                    return
        messagebox.showinfo("teade", "pildid on salvestatud.")
aken = tk.Tk()
aken.title("pildid")
aken.geometry("450x400")
failide_nimed = tk.StringVar()
silt = tk.Label(aken, text="vali pildid et neid salvestada.")
silt.pack(pady=10)
tekstiväli = tk.Label(aken, textvariable=failide_nimed, justify="left", width=50, height=10, anchor="w", relief="sunken")
tekstiväli.pack(pady=10)
valige_failid_nupp = tk.Button(aken, text="vali failid", command=valige_failid)
valige_failid_nupp.pack(pady=10)
salvesta_pildid_nupp = tk.Button(aken, text="salvesta pildid", command=salvestage_pildid)
salvesta_pildid_nupp.pack(pady=10)
aken.mainloop()