import tkinter as tk
from tkinter import ttk
import db

db.create_tables()

modules = db.get_modules()
print(len(modules), "modules gevonden")

root = tk.Tk()
root.title("Studieplanner")

tabel = ttk.Treeview(root, columns=("id", "naam", "omschrijving"), show="headings", height=10)
tabel.heading("id", text="ID")
tabel.heading("naam", text="Naam")
tabel.heading("omschrijving", text="Omschrijving")
tabel.column("id", width=50)
tabel.pack(fill="both", expand=True)

for module in db.get_modules():
    tabel.insert("", tk.END, values=(module["id"], module["naam"], module["omschrijving"]))

root.mainloop()