import tkinter as tk
from tkinter import messagebox
from scrap import Scrap
from tkinter import ttk
import pandas as pd
from check_data import check_data

def scrape_website():
    url = 'https://www.muasah.org.sa/rafed/'
    username = username_entry.get()
    password = password_entry.get()
    count = int(count_entry.get())
    
    try:
        scrap = Scrap(url, username, password, count)
        messagebox.showinfo("ممتاز", "تمت العملية بنجاح!")
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
        for i, row in enumerate(df.iterrows):
            values = [str(row[j]) for j in range(1, len(columns))]
            tree.insert("", "end", iid=i, values=values)

    except FileNotFoundError:
        messagebox.showerror("لا يوجد ملف", "البيانات غير متوفرة.")

# Create the main window
root = tk.Tk()
root.title("أداة استيراد البيانات من الموقع")
root.geometry("800x600")
style = ttk.Style()
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
style.configure("TWindow",
                background="#ECECEC")
style.configure("TLabel",
                background="#ECECEC",
                foreground="#333333",
                font=("Helvetica", 13))
style.configure("TEntry",
                fieldbackground="#F0F0F0",
                font=("Helvetica", 13),
                )
style.configure("TButton",
                background="#4CAF50",  # Green background
                foreground="#FFFFFF",  # White text color
                font=("Helvetica", 14),
                padding=10)
# Create and position the labels
username_label = ttk.Label(root, text=":اسم المستخدم", style="TLabel")
username_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")

password_label = ttk.Label(root, text=":كلمة المرور", style="TLabel")
password_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")

count_label = ttk.Label(root, text=":عدد السجلات", style="TLabel")
count_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

# Create and position the entry fields
username_entry = ttk.Entry(root, style="TEntry")
username_entry.grid(row=1, column=0, padx=10, pady=5)

password_entry = ttk.Entry(root, show="*", style="TEntry")
password_entry.grid(row=2, column=0, padx=10, pady=5)

count_entry = ttk.Entry(root, style="TEntry")
count_entry.grid(row=3, column=0, padx=10, pady=5)

# Create and position the scrape button
scrape_button = ttk.Button(root, text="استيراد", command=scrape_website, style="TButton")
scrape_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

check_button = ttk.Button(root,text='فحص الأخطاء',command=check_data)
check_button.grid(row=4, column=2, padx=10, pady=10)

# Create a Treeview widget
columns = [
    "الرقم",
    "الاسم",
    "الجنس"
]
tree = ttk.Treeview(root, columns=columns, show="headings", style="Treeview")

# Configure the Treeview columns
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor='center')

# Create a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Create a button to show the table
show_button = ttk.Button(root, text="عرض المتوفين", command=show_table, style="TButton")

# Grid layout
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
scrollbar.grid(row=5, column=2, padx=(0, 10), pady=10, sticky="ns")
show_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Configure the grid weights
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the main loop
root.mainloop()