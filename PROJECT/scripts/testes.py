import unittest
from unittest.mock import MagicMock, patch
from tutorial import criar_tutorial
from menu import criar_menu

#TODO: colocar os demais testes aqui
def pular_tutorial():
    janela.destroy()  # Fecha a janela de tutorial quando chamada

class TestTutorialSecundaria(unittest.TestCase):
    @patch("tutorial.tk.Tk")
    def test_criar_tutorial_secundaria(self, mock_tk):
        global janela  # Defina janela como uma variável global
        janela = criar_tutorial(pular_tutorial)
        mock_tk.assert_called()

class TestMenuPrincipal(unittest.TestCase):
    @patch("menu.tk.Tk")
    @patch("menu.tk.Label")
    def test_criar_menu_principal(self, mock_label, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance

        criar_menu()

        mock_tk.assert_called()
        mock_label.assert_called_with(mock_tk_instance, text="Jogo da Senha", font=("Times New Roman", 60), fg="#00FFFF", bg="#000315")

if __name__ == "__main__":
    unittest.main()
