import tkinter as tk
import secrets
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho))
    return senha

def atualizar_senha():
    nova_senha = gerar_senha()
    senha_var.set(nova_senha)

def copiar_senha():
    root.clipboard_clear()
    root.clipboard_append(senha_var.get())
    root.update()  # Atualiza a área de transferência

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Senha")

# Configurações de estilo
root.configure(bg="#f0f0f0")

# Título
titulo = tk.Label(root, text="Gerador de Senha Forte", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333333")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Instruções
instrucoes = tk.Label(root, text="Clique no botão abaixo para gerar uma nova senha", font=("Helvetica", 12), bg="#f0f0f0", fg="#666666")
instrucoes.grid(row=1, column=0, columnspan=2, pady=5)

# Label para mostrar a senha
senha_var = tk.StringVar()
senha_var.set(gerar_senha())
senha_label = tk.Label(root, textvariable=senha_var, font=("Helvetica", 16), bg="white", relief="sunken", width=40, padx=10, pady=5)
senha_label.grid(row=2, column=0, columnspan=2, pady=20)

# Botão para gerar uma nova senha
gerar_btn = tk.Button(root, text="Gerar Nova Senha", command=atualizar_senha, font=("Helvetica", 14), bg="#4CAF50", fg="#ffffff", activebackground="#45a049", relief="raised")
gerar_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Botão para copiar a senha

copiar_btn = tk.Button(root, text="Copiar Senha", command=copiar_senha, font=("Helvetica", 14), bg="#2196F3", fg="#ffffff", activebackground="#0b79d0", relief="raised")
copiar_btn.grid(row=4, column=0, columnspan=2, pady=10)

# Executar o loop da interface gráfica
root.mainloop()
