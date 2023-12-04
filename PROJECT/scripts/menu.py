import tkinter as tk
from partida import iniciar_jogo
from tutorial import criar_tutorial
#TODO: implementar botao para ir no tutorial 
def criar_menu():
    menu = tk.Tk()
    menu.title("Jogo da Senha")
    menu.iconbitmap("PROJECT/icon/window_icon.ico")
    menu.resizable(True, True)
    menu.geometry("750x500")
    menu.configure(background="#7D5B8C")
    
    menu_text = tk.Label(menu, text="Jogo da Senha", font=("Times New Roman", 60), fg="#470064", bg="#7D5B8C")
    menu_text.pack(pady=(20, 0))  # Use pady para definir o espaço acima do widget

    iniciar_jogo_button = tk.Button(menu, bg="#B19CD9", fg="black", text="Iniciar Jogo", command=lambda: iniciar_jogo(), width=15, font=("Times New Roman", 20))
    iniciar_jogo_button.pack(pady=55)

    tutorial_button = tk.Button(menu, bg="#B19CD9", fg="black", text="Tutorial", command=lambda: criar_tutorial(), width=15, font=("Times New Roman", 20))
    tutorial_button.pack(pady=30)

    menu.mainloop()
    return menu

criar_menu()
