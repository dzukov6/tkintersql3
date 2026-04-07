import tkinter as tk

aken = tk.Tk()

# Akna pealkirja lisamine
aken.title("Daniel ulesanded")

# Akna suuruse määramine (laius x kõrgus)
aken.geometry("400x400")

# Akna suuruse ja asukoha määramine (laius x kõrgus + x + y)
aken.geometry("400x400+100+100")

# Akna suuruse muutmise keelamine
aken.resizable(False, False)

# Akna läbipaistvuse seadistamine (väärtus vahemikus 0.0 kuni 1.0)
aken.attributes('-alpha', 0.9)
aken.mainloop()