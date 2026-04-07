import tkinter as tk

def kuva_varv(varv):
    tulemus_label.config(text=varv, font=("Arial", 20))

aken = tk.Tk()
aken.title("Värvi nupud")
aken.geometry("500x200")

tulemus_label = tk.Label(aken, text="", font=("Arial", 20))
tulemus_label.pack(side="bottom", pady=20)
nupp1 = tk.Button(aken, bg="red", command=lambda: kuva_varv("punane"))
nupp1.pack(side="right", expand=True, fill="both")
nupp2 = tk.Button(aken, bg="green", command=lambda: kuva_varv("roheline"))
nupp2.pack(side="right", expand=True, fill="both")
nupp3 = tk.Button(aken, bg="blue", command=lambda: kuva_varv("sinine"))
nupp3.pack(side="right", expand=True, fill="both")
nupp4 = tk.Button(aken, bg="yellow", command=lambda: kuva_varv("kollane"))
nupp4.pack(side="right", expand=True, fill="both")
nupp5 = tk.Button(aken, bg="orange", command=lambda: kuva_varv("oranz"))
nupp5.pack(side="right", expand=True, fill="both")

aken.mainloop()