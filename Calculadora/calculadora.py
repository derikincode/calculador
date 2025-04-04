import tkinter as tk
from ttkbootstrap import Style

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Moderna")
        self.root.geometry("300x100")
        
        style = Style("superhero")  # Tema moderno
        
        self.expr = ""
        self.result_var = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 18), justify='right', bd=10, relief=tk.FLAT)
        self.display.pack(fill='both', padx=10, pady=10)
        self.display.bind("<KeyRelease>", self.update_expression)

    def update_expression(self, event):
        try:
            value = float(self.display.get())
            value_with_10_percent = value * 1.10
            self.result_var.set(f"{value_with_10_percent:.2f}")
        except ValueError:
            self.result_var.set("")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
