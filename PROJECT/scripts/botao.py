import tkinter as tk
from tkinter import messagebox
from senha import gerar_senha, proximidade

NUM_CORES_SENHA = 4
cores_disponiveis = ["red", "green", "blue", "yellow"][:NUM_CORES_SENHA]
sequencia_correta = gerar_senha(NUM_CORES_SENHA, cores_disponiveis)
tentativa_atual = []
tentativas_restantes = 7
historico_canvas = None
tentativas_anteriores = None
chosen_colors_canvas = None
tentativas_label = None
historico_rectangles = []

def botao_cor_clicado(cor):
    if len(tentativa_atual) < NUM_CORES_SENHA:
        tentativa_atual.append(cor)
        update_chosen_colors_canvas()


def mostrar_senha_correta():
    senha_correta = ", ".join(sequencia_correta)
    messagebox.showinfo("Senha Correta", f"A senha correta é: {senha_correta}")


def deletar_cor():
    if tentativa_atual:
        tentativa_atual.pop()
        update_chosen_colors_canvas()


def resetar_sequencia():
    global tentativa_atual
    tentativa_atual = []
    update_chosen_colors_canvas()

def enviar_sequencia():
    verificar_sequencia()

def verificar_sequencia():
    global tentativas_restantes
    if len(tentativa_atual) < NUM_CORES_SENHA:
        messagebox.showwarning("Aviso", "Complete a tentativa antes de enviar a senha")
        return
    tentativas_restantes -= 1
    tentativas_anteriores.append(list(tentativa_atual))
    historico_rectangles.append(list(tentativa_atual))
    update_historico_canvas()
    tentativas_label.config(text=f"Tentativas restantes: {tentativas_restantes}")
    if tuple(tentativa_atual) == tuple(sequencia_correta):
        messagebox.showinfo("Parabéns!", "Você acertou a senha")
        reiniciar_jogo()
    elif tentativas_restantes == 0:
        messagebox.showinfo("Que pena!", "Suas tentativas acabaram")
        mostrar_senha_correta()
        reiniciar_jogo()
    else:
        messagebox.showerror(" ", "Você errou")
    resetar_sequencia()


def reiniciar_jogo():
    global sequencia_correta, tentativa_atual, tentativas_anteriores, historico_rectangles, tentativas_restantes
    sequencia_correta = gerar_senha(NUM_CORES_SENHA, cores_disponiveis)
    tentativa_atual = []
    tentativas_restantes = 7
    tentativas_anteriores = []
    historico_rectangles = []
    chosen_colors_canvas.delete("all")
    historico_canvas.delete("all")
    tentativas_label.config(text=f"Tentativas restantes: {tentativas_restantes}")



def update_chosen_colors_canvas():
    chosen_colors_canvas.delete("all")
    for i, cor in enumerate(tentativa_atual):
        x1 = i*40
        y1 = 0
        x2 = (i+1)*40
        y2 = 40
        chosen_colors_canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline=cor)

def update_historico_canvas():
    historico_canvas.delete("all")
    
    tamanho_circulo = 30  # Tamanho do círculo para exibir as cores de feedback
    espacamento = 5  # Espaçamento entre os círculos

    for i, tentativa in enumerate(historico_rectangles):
        for j, cor in enumerate(tentativa):
            x1 = j * 40
            y1 = i * 40
            x2 = (j + 1) * 40
            y2 = (i + 1) * 40
            historico_canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline=cor)

        # Adicione as dicas utilizando a função proximidade
        dicas = proximidade(tentativa, sequencia_correta)
        for k, dica_cor in enumerate(dicas):
            x_centro = (NUM_CORES_SENHA + k) * 40 + tamanho_circulo / 2 + espacamento
            y_centro = i * 40 + tamanho_circulo / 2
            historico_canvas.create_oval(
                x_centro - tamanho_circulo / 2, y_centro - tamanho_circulo / 2,
                x_centro + tamanho_circulo / 2, y_centro + tamanho_circulo / 2,
                fill=dica_cor, outline=dica_cor
            )
def iniciar_jogo(menu):
    global sequencia_correta, tentativa_atual, tentativas_restantes, tentativas_anteriores, chosen_colors_canvas, tentativas_label, historico_canvas
    
    # Feche a janela do menu antes de abrir a do jogo
    menu.destroy()

    root = tk.Tk()
    root.title("Jogo do Senha")

    root.resizable(True, True)
    root.geometry("750x500")
    root.configure(background="#000315")

    menu_text = tk.Label(root, text="Jogo da Senha", font=("Times New Roman", 30), fg="#00FFFF", bg="#000315")
    menu_text.pack(pady=(20, 0))

    chosen_colors_canvas = tk.Canvas(root, bg="#000315", width=NUM_CORES_SENHA * 40, height=40)
    chosen_colors_canvas.pack(side=tk.TOP)

    # historico com espaço para botar as dicas
    historico_canvas = tk.Canvas(root, bg="#000315", width=NUM_CORES_SENHA*80, height=tentativas_restantes*40)
    historico_canvas.pack(side=tk.TOP)

    tentativas_label = tk.Label(root, bg="#000315", fg='white', text="Tentativas restantes: 7")
    tentativas_label.pack()

    for cor in cores_disponiveis:  # Alterado para usar cores_disponiveis
        cor_button = tk.Button(root, bg=cor, width=10, height=2, command=lambda c=cor: botao_cor_clicado(c))
        cor_button.pack(side=tk.LEFT, padx=5, pady=5)

    reiniciar_button = tk.Button(root, bg='#000315', fg='white', text='Reiniciar', command=reiniciar_jogo)
    reiniciar_button.pack(side=tk.RIGHT, padx=5)

    resetar_button = tk.Button(root, bg="#000315", fg='white', text="Resetar", command=resetar_sequencia)
    resetar_button.pack(side=tk.RIGHT, padx=5)

    deletar_button = tk.Button(root, bg="#000315", fg='white', text="Deletar", command=deletar_cor)
    deletar_button.pack(side=tk.RIGHT, padx=5)

    enviar_button = tk.Button(root, bg="#000315", fg='white', text="Enviar", command=enviar_sequencia)
    enviar_button.pack(side=tk.RIGHT, padx=5)

    sequencia_correta = gerar_senha(NUM_CORES_SENHA, cores_disponiveis)

    tentativa_atual = []

    tentativas_restantes = 7

    tentativas_anteriores = []

    root.mainloop()

