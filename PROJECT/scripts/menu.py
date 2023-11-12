import tkinter as tk
import ctypes
from botao import iniciar_jogo
#TODO: implementar botoes de ir para a partida e de ir para o tutorial 
def criar_menu():
    menu = tk.Tk()
    myappId = "Jogo da Senha"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappId)
    menu.title("Jogo da Senha")
    menu.iconbitmap("PROJECT/icon/window_icon.ico")
    menu.resizable(True, True)
    menu.geometry("750x500")
    menu.configure(background="#000315")
    
    menu_text = tk.Label(menu, text="Jogo da Senha", font=("Times New Roman", 60), fg="#00FFFF", bg="#000315")
    menu_text.pack(pady=(20, 0))  # Use pady para definir o espaço acima do widget

    iniciar_jogo_button = tk.Button(menu, bg = "#000315", fg = "white", text="Iniciar Jogo", command=iniciar_jogo, width=15, font=("Times New Roman", 20))
    iniciar_jogo_button.pack(pady=30)

    menu.mainloop()
    return menu

criar_menu()
