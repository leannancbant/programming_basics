import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    root.geometry(f"{width}x{height}")
    root.title("Studieplanner")

    root.mainloop()

if __name__ == '__main__':
    main()