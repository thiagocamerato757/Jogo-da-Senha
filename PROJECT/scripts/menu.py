import tkinter as tk
import ctypes
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

    menu.mainloop()
    return menu
