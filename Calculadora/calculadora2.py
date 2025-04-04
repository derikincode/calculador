import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label, Combobox, Frame, Separator
import tkinter.messagebox as msgbox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Porcentagem")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.style = Style("darkly")  # Tema inicial escuro
        
        self.icon = tk.PhotoImage(file="grafico.png")
        self.root.iconphoto(True, self.icon)

        self.valor_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.porcentagem_var = tk.StringVar(value="10%")
        self.history = []
        
        self.create_widgets()

    def create_widgets(self):
        frame = Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        Label(frame, text="Digite o valor do produto:", font=("Arial", 11)).pack(pady=5)
        
        self.entry_valor = Entry(frame, textvariable=self.valor_var, font=("Arial", 14), 
                                 bootstyle="success", width=20)
        self.entry_valor.pack(pady=5)
        self.entry_valor.insert(0, "Ex: 100.00")  # Placeholder
        
        # Adicionando comportamento de limpar o placeholder ao clicar
        self.entry_valor.bind("<FocusIn>", self.clear_placeholder)
        self.entry_valor.bind("<FocusOut>", self.add_placeholder)

        Label(frame, text="📊 Escolha a porcentagem:", font=("Arial", 11)).pack(pady=5)
        
        porcentagens = ["5%", "10%", "15%", "20%", "25%", "50%", "75%", "100%"]
        self.combobox = Combobox(frame, textvariable=self.porcentagem_var, values=porcentagens,
                                 font=("Arial", 12), state="readonly", bootstyle="info")
        self.combobox.pack(pady=5)

        btn_frame = Frame(frame)
        btn_frame.pack(pady=10)

        Button(btn_frame, text="Calcular %", command=self.calcular_porcentagem,
               bootstyle="primary-outline", width=12).grid(row=0, column=0, padx=5)

        Button(btn_frame, text="+ Porcentagem", command=self.calcular_soma,
               bootstyle="info-outline", width=12).grid(row=0, column=1, padx=5)

        Button(btn_frame, text="- Porcentagem", command=self.calcular_subtracao,
               bootstyle="warning-outline", width=12).grid(row=1, column=0, padx=5, pady=5)

        Button(btn_frame, text="Limpar", command=self.limpar_campos,
               bootstyle="danger-outline", width=12).grid(row=1, column=1, padx=5, pady=5)
        
        Button(frame, text="📜 Ver Histórico", command=self.mostrar_historico,
               bootstyle="secondary-outline", width=25).pack(pady=5)
        
        Separator(frame).pack(fill="x", pady=10)
        
        Label(frame, textvariable=self.result_var, font=("Arial", 12), wraplength=350,
              justify="center").pack(pady=15)
        
        Button(frame, text="🔄 Alternar Tema", command=self.alternar_tema,
               bootstyle="light-outline", width=25).pack(pady=5)

    def clear_placeholder(self, event):
        if self.entry_valor.get() == "Ex: 100.00":
            self.entry_valor.delete(0, tk.END)

    def add_placeholder(self, event):
        if not self.entry_valor.get():
            self.entry_valor.insert(0, "Ex: 100.00")

    def get_valores(self):
        try:
            valor_str = self.valor_var.get().replace(",", ".")
            valor = float(valor_str) if valor_str.replace(".", "").isdigit() else None

            porcentagem_str = self.porcentagem_var.get().replace("%", "")
            porcentagem = float(porcentagem_str)

            if valor is None:
                raise ValueError
            
            return valor, porcentagem
        except ValueError:
            self.result_var.set("⚠️ Digite um número válido!")
            return None, None

    def calcular_porcentagem(self):
        valor, porcentagem = self.get_valores()
        if valor is not None:
            resultado = valor * (porcentagem / 100)
            self.atualizar_resultado(f"📈 {porcentagem:.0f}% de {valor:.2f} = {resultado:.2f}", resultado)

    def calcular_soma(self):
        valor, porcentagem = self.get_valores()
        if valor is not None:
            resultado = valor + (valor * porcentagem / 100)
            self.atualizar_resultado(f"➕ {valor:.2f} + {porcentagem:.0f}% = {resultado:.2f}", resultado)

    def calcular_subtracao(self):
        valor, porcentagem = self.get_valores()
        if valor is not None:
            resultado = valor - (valor * porcentagem / 100)
            self.atualizar_resultado(f"➖ {valor:.2f} - {porcentagem:.0f}% = {resultado:.2f}", resultado)

    def limpar_campos(self):
        self.valor_var.set("")
        self.result_var.set("")
        self.porcentagem_var.set("10%")
        self.add_placeholder(None)

    def atualizar_resultado(self, texto, resultado):
        self.result_var.set(texto)
        self.history.append(texto)

        # Copiar automaticamente apenas o resultado numérico
        self.root.clipboard_clear()
        self.root.clipboard_append(f"{resultado:.2f}")
        self.root.update()  # Garante que a cópia seja reconhecida pelo sistema

    def mostrar_historico(self):
        if not self.history:
            msgbox.showinfo("Histórico", "Nenhum cálculo realizado ainda.")
        else:
            historico_texto = "\n".join(self.history[-5:])  # Mostra os últimos 5 cálculos
            msgbox.showinfo("Histórico de Cálculos", historico_texto)

    def alternar_tema(self):
        if self.style.theme.name == "darkly":
            self.style.theme_use("flatly")  # Modo claro
        else:
            self.style.theme_use("darkly")  # Modo escuro

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
