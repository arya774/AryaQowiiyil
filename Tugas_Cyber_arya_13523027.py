import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    text_area.delete(1.0, tk.END)


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Success", "File saved successfully!")


def delete_file():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete the content?"):
        text_area.delete(1.0, tk.END)


# Creating main window
app = tk.Tk()
app.title("Simple Notepad")
app.geometry("600x400")

# Creating a text area
text_area = tk.Text(app, wrap="word", undo=True)
text_area.pack(fill="both", expand=True)

# Creating a menu bar
menu_bar = tk.Menu(app)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Delete", command=delete_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Adding menu to window
app.config(menu=menu_bar)

# Running the application
app.mainloop()