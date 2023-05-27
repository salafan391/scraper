import tkinter as tk
from tkinter import messagebox
from scrap import Scrap
def scrape_website():
    url = 'https://www.muasah.org.sa/rafed/'
    username = username_entry.get()
    password = password_entry.get()
    count = int(count_entry.get())
    try:
        scrap = Scrap(url, username, password, count)
        msg = messagebox.showinfo("ممتاز", "تمت العملية بنجاح!")
        if msg:
            window.quit()
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Close the loading window and re-enable the scrape button
# Create the main window
window = tk.Tk()
window.title("استيراد البيانات")

# Create and position the labels


username_label = tk.Label(window, text="اسم المستخدم:")
username_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")

password_label = tk.Label(window, text="كلمة المرور:")
password_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")

count_label = tk.Label(window, text="عدد السجلات:")
count_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

# Create and position the entry fields

username_entry = tk.Entry(window)
username_entry.grid(row=1, column=0, padx=10, pady=5)

password_entry = tk.Entry(window, show="*")
password_entry.grid(row=2, column=0, padx=10, pady=5)

count_entry = tk.Entry(window)
count_entry.grid(row=3, column=0, padx=10, pady=5)

# Create and position the scrape button
scrape_button = tk.Button(window, text="استيراد", command=scrape_website)
scrape_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()
