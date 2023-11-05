import unittest
from unittest.mock import MagicMock, patch
from tutorial import criar_tutorial
from menu import criar_menu
from senha import gerar_senha


#TODO: colocar os demais testes aqui

class TestGerarCombinacaoCores(unittest.TestCase):
    def test_gerar_senha(self):
        # Caso de teste 1: Verificar se o número de cores gerado é igual ao número especificado
        num_cores = 6
        cores_disponiveis = ["vermelho", "verde", "azul", "amarelo", "roxo", "laranja"]
        combinacao = gerar_senha(num_cores, cores_disponiveis)
        self.assertEqual(len(combinacao), num_cores)

        # Caso de teste 2: Verificar se todas as cores na combinação são únicas
        num_cores = 3
        cores_disponiveis = ["vermelho", "verde", "azul"]
        combinacao = gerar_senha(num_cores, cores_disponiveis)
        self.assertEqual(len(combinacao), len(set(combinacao)))

        # Caso de teste 3: Verificar se a função lida corretamente com 0 cores
        num_cores = 0
        cores_disponiveis = ["vermelho", "verde", "azul"]
        combinacao = gerar_senha(num_cores, cores_disponiveis)
        self.assertEqual(len(combinacao), 0)

        # Caso de teste 4: Verificar se a função lida corretamente com um grande número de cores
        num_cores = 1000
        cores_disponiveis = ["vermelho", "verde", "azul"] * 1000  # Uma lista grande de cores
        combinacao = gerar_senha(num_cores, cores_disponiveis)
        self.assertEqual(len(combinacao), num_cores)

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
