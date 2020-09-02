import tkinter as tk

# WINDOW
window = tk.Tk()
window.title("App")
window.geometry("1280x950")

# FUNCTIONS


def func():
    pass


def text_display():
    text = func()
    text_display = tk.Text(master=window, height=10, width=25)
    text_display.grid(row=3, column=1)
    text_display.insert(tk.END, text)


# LABEL
label1 = tk.Label(master=window, text="Welcome to My APP",
                  font=("Times New Roman", 25))
label1.grid(row=0, column=0)

label2 = tk.Label(master=window, text="What's your name? ")
label2.grid(row=1, column=0)

# ENTRY FIELD
entryfield1 = tk.Entry()
entryfield1.grid(row=1, column=1)

# BUTTON
button1 = tk.Button(text="Click Here", bg='red', command=text_display)
button1.grid(row=2, column=1)

# TEXT FIELD
textfield1 = tk.Text(master=window, height=10, width=30)
textfield1.grid(row=2, column=0)

# Make the frame to appear on the screen
window.mainloop()
