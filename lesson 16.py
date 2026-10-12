import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Books and Authors")
root.geometry("500x300")

title_label = tk.Label(root, text="Books and Authors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

tree = ttk.Treeview(root, columns=("Book", "Author"), show="headings")

tree.heading("Book", text="Book Title")
tree.heading("Author", text="Author")

tree.column("Book", width=250)
tree.column("Author", width=200)

books = [
    ("Harry Potter", "J.K. Rowling"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Wonder", "R.J. Palacio"),
    ("Matilda", "Roald Dahl"),
    ("Charlotte's Web", "E.B. White")
]

for book in books:
    tree.insert("", tk.END, values=book)

tree.pack(pady=10, padx=10, fill="both", expand=True)

root.mainloop()