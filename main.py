import Tkinter as tk

window = tk.Tk()
window.title("Joonas Database")

info = tk.Label(text = "This will be my database later on. 2025 Joonas Lindberg",
height = 9,
anchor = "w",
justify = "left")
info.grid(row = 0, column = 0)

window.mainloop()
