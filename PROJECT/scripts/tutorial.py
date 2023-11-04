import tkinter as tk
import ctypes
import unittest

def criar_tutorial():
    def pular_tutorial():
        tutorial.destroy()

    tutorial = tk.Tk()
    myappId = "Jogo da Senha"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappId)
    tutorial.title("Jogo da Senha")
    tutorial.iconbitmap("PROJECT/icon/window_icon.ico")
    tutorial.resizable(True, True)
    tutorial.geometry("750x500")
    tutorial.configure(background="#000315")
    
    # Abra o arquivo com codificação UTF-8
    with open("PROJECT\\arqs\\tutorial.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    # Crie um widget Text para exibir o conteúdo do tutorial
    texto_tutorial = tk.Text(tutorial, wrap="word", font=("Times New Roman", 18), fg="#FFFFFF", bg="#000315", bd=0)
    texto_tutorial.insert("1.0", conteudo)
    texto_tutorial.pack(fill="both", expand=True)

    # Crie um botão "Pular Tutorial" para fechar a janela
    botao_pular = tk.Button(tutorial, text="Pular Tutorial", command=pular_tutorial, height=2, width=20)
    botao_pular.pack(pady=50)

    tutorial.mainloop()
    return tutorial

class TestTutorialSecundaria(unittest.TestCase):
    def test_criar_tutorial_secundaria(self):
        tutorial = criar_tutorial()
        self.assertIsInstance(tutorial, tk.Tk)
        self.assertEqual(tutorial.winfo_exists(), 1)
        tutorial.destroy()
        tutorial.quit()

if __name__ == "__main__":
    unittest.main()
