import tkinter as tk
def criar_tutorial(pular_callback=None):
    def pular_tutorial():
        if pular_callback:
            pular_callback()
        tutorial.destroy()

    tutorial = tk.Tk()
    tutorial.title("Jogo da Senha")
    tutorial.iconbitmap("PROJECT/icon/window_icon.ico")
    tutorial.resizable(True, True)
    tutorial.geometry("750x500")
    tutorial.configure(background="#7D5B8C")
    
    # Abra o arquivo com codificação UTF-8
    with open("PROJECT\\arqs\\tutorial.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    # Crie um widget Text para exibir o conteúdo do tutorial
    texto_tutorial = tk.Text(tutorial, wrap="word", font=("Times New Roman", 18), fg="black", bg="#7D5B8C", bd=0)
    texto_tutorial.insert("1.0", conteudo)
    texto_tutorial.pack(fill="both", expand=True)

    # Crie um botão "Pular Tutorial" para fechar a janela
    botao_pular = tk.Button(tutorial, text="Sair do Tutorial", bg="#B19CD9", command=pular_tutorial, height=2, width=20)
    botao_pular.pack(pady=50)

    tutorial.mainloop()
    return tutorial
