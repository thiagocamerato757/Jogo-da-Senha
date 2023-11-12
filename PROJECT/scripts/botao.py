import tkinter as tk
from tkinter import messagebox
from senha import gerar_senha

def botao_cor_clicado(cor):
    global tentativa_atual
    tentativa_atual.append(cor)
    update_chosen_colors_label()

def mostrar_senha_correta():
    senha_correta = ", ".join(sequencia_correta)
    messagebox.showinfo("Senha Correta", f"A senha correta é: {senha_correta}")

def deletar_cor():
    global tentativa_atual
    if tentativa_atual:
        tentativa_atual.pop()
        update_chosen_colors_label()

def resetar_sequencia():
    global tentativa_atual
    tentativa_atual = []
    update_chosen_colors_label()

def enviar_sequencia():
    verificar_sequencia()

def verificar_sequencia():
    global tentativas_restantes, tentativa_atual, historico_text, tentativas_anteriores
    tentativas_restantes -= 1
    tentativas_anteriores.append(list(tentativa_atual))
    historico_text.insert(tk.END, f"Tentativa {len(tentativas_anteriores)}: {'. '.join(tentativa_atual)}\n")
    tentativas_label.config(text=f"Tentativas restantes: {tentativas_restantes}")
    if tuple(tentativa_atual) == tuple(sequencia_correta):
        messagebox.showinfo("Parabéns!","Você acertou a senha")
    elif tentativas_restantes == 0:
        messagebox.showinfo("Que pena!", "Suas tentativas acabaram")
        mostrar_senha_correta()
        reiniciar_jogo()
    else:
        messagebox.showerror(" ", "Você errou")
    resetar_sequencia()

def reiniciar_jogo():
    global sequencia_correta, tentativa_atual, tentativas_restantes, tentativas_anteriores
    sequencia_correta = gerar_senha(4, cores)
    tentativa_atual = []
    tentativas_restantes = 5
    tentativas_anteriores = []

    chosen_colors_label.config(text="Cores Escolhidas: ")
    historico_text.delete(1.0, tk.END)
    tentativas_label.config(text=f"Tentativas restantes: {tentativas_restantes}")

def update_chosen_colors_label():
    chosen_colors_label.config(text="Cores Escolhidas: " + ", ".join(tentativa_atual))

cores = ["red", "green", "blue", "yellow"]

def iniciar_jogo():
    global sequencia_correta, tentativa_atual, tentativas_restantes, tentativas_anteriores, chosen_colors_label, tentativas_label, historico_text
    root = tk.Tk()
    root.title("Jogo do Senha")

    root.resizable(True, True)
    root.geometry("750x500")
    root.configure(background="#000315")

    menu_text = tk.Label(root, text="Jogo da Senha", font=("Times New Roman", 30), fg="#00FFFF", bg="#000315")
    menu_text.pack(pady=(20, 0))

    chosen_colors_label = tk.Label(root, bg = "#000315", fg = 'white', text="Cores Escolhidas: ")
    chosen_colors_label.pack(side=tk.TOP)

    historico_text=tk.Text(root, bg = "#000315", fg= 'white', height=10, width=50)
    historico_text.pack(side=tk.TOP)

    tentativas_label = tk.Label(root, bg = "#000315", fg = 'white', text="Tentativas restantes: 5")
    tentativas_label.pack()

    for cor in cores: 
        cor_button = tk.Button(root, bg = cor, width = 10, height = 2, command=lambda c=cor: botao_cor_clicado(c))
        cor_button.pack(side=tk.LEFT, padx=5, pady=5)

    deletar_button = tk.Button(root, bg = "#000315", fg = 'white', text="Deletar", command=deletar_cor)
    deletar_button.pack(side=tk.RIGHT, padx=5)

    resetar_button = tk.Button(root, bg = "#000315", fg = 'white', text="Resetar", command=resetar_sequencia)
    resetar_button.pack(side=tk.RIGHT, padx=5)

    enviar_button = tk.Button(root, bg = "#000315", fg = 'white', text="Enviar", command=enviar_sequencia)
    enviar_button.pack(side=tk.RIGHT, padx=5)

    reiniciar_button = tk.Button(root, bg='#000315', fg='white', text='Reiniciar', command=reiniciar_jogo)
    reiniciar_button.pack(side=tk.RIGHT, padx=5)

    sequencia_correta = gerar_senha(4, cores)

    tentativa_atual = []

    tentativas_restantes = 5

    tentativas_anteriores = []

    root.mainloop()