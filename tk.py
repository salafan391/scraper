import tkinter as tk
from tkinter import messagebox
from scrap import Scrap
from tkinter import ttk
import pandas as pd

def scrape_website():
    url = 'https://www.muasah.org.sa/rafed/'
    username = username_entry.get()
    password = password_entry.get()
    count = int(count_entry.get())
    try:
        scrap = Scrap(url, username, password, count)
        msg = messagebox.showinfo("ممتاز", "تمت العملية بنجاح!")
        if msg:
            root.quit()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_table():
    try:
        # Clear existing data
        tree.delete(*tree.get_children())

        # Read the CSV file
        df = pd.read_csv('rafed_data.csv')

        # Insert data into the treeview
        for _, row in df.iterrows():
            values = [str(row[i]) for i in range(len(columns))]
            tree.insert("", "end", values=values)

    except FileNotFoundError:
        messagebox.showerror("لا يوجد ملف", "البيانات غير متوفرة.")


# Create the main window
root = tk.Tk()
root.title("أداة استيراد البيانات من الموقع")
root.geometry("800x600")  # Set the window size

# Create and position the labels
username_label = tk.Label(root, text="اسم المستخدم:")
username_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")

password_label = tk.Label(root, text="كلمة المرور:")
password_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")

count_label = tk.Label(root, text="عدد السجلات")
count_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

# Create and position the entry fields
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=0, padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=0, padx=10, pady=5)

count_entry = tk.Entry(root)
count_entry.grid(row=3, column=0, padx=10, pady=5)

# Create and position the scrape button
scrape_button = tk.Button(root, text="استيراد", command=scrape_website)
scrape_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Create a Treeview widget
columns = [
    "الرقم",
    "الاسم",
    "الجنس"
]
tree = ttk.Treeview(root, columns=columns, show="headings")

# Configure the Treeview columns
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

# Create a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Create a button to show the table
show_button = ttk.Button(root, text="عرض المتوفين", command=show_table)

# Grid layout
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
scrollbar.grid(row=5, column=2, padx=(0, 10), pady=10, sticky="ns")
show_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Configure the grid weights
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the main loop
root.mainloop()