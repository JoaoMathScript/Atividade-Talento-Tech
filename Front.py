import tkinter as tk
from tkinter import ttk

class JanelaBonita:
    def __init__(self, root):
        self.root = root
        self.root.title("Janela Bonita")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")
        
        self.criar_widgets()

    def criar_widgets(self):
        # Título
        titulo = tk.Label(self.root, text="Bem-vindo!", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#4b0082")
        titulo.pack(pady=10)
        
        # Caixa de texto
        self.caixa_texto = tk.Text(self.root, height=5, width=40, wrap=tk.WORD, font=("Arial", 12))
        self.caixa_texto.pack(pady=10)
        
        # Botões
        btn_frame = tk.Frame(self.root, bg="#f0f8ff")
        btn_frame.pack(pady=10)
        
        botao_mostrar = ttk.Button(btn_frame, text="Mostrar Texto", command=self.mostrar_texto)
        botao_mostrar.grid(row=0, column=0, padx=5)

        botao_limpar = ttk.Button(btn_frame, text="Limpar Texto", command=self.limpar_texto)
        botao_limpar.grid(row=0, column=1, padx=5)
        
        # Label de resultado
        self.resultado = tk.Label(self.root, text="", bg="#f0f8ff", fg="#4b0082", font=("Arial", 12))
        self.resultado.pack(pady=10)

    def mostrar_texto(self):
        texto = self.caixa_texto.get("1.0", tk.END).strip()
        if texto:
            self.resultado.config(text=f"Você digitou: {texto}")
        else:
            self.resultado.config(text="A caixa de texto está vazia.")
    
    def limpar_texto(self):
        self.caixa_texto.delete("1.0", tk.END)
        self.resultado.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaBonita(root)
    root.mainloop()
