import unittest
from src.app import criar_usuario, listar_usuarios, deletar_usuario, buscar_usuario, usuarios

class TestCRUDUsuarios(unittest.TestCase):

    def test_criar_usuario(self):
        resultado = criar_usuario("João", "joao@email.com", "1234", "11111111111")
        self.assertEqual(resultado, "Usuário criado com sucesso.")
        self.assertEqual(len(usuarios), 2)

    def test_listar_usuarios(self):
        criar_usuario("Maria", "maria@email.com", "abcd", "22222222222")
        usuarios = listar_usuarios()
        self.assertEqual(len(usuarios), 3)

    def test_buscar_usuario_por_cpf(self):
        criar_usuario("Pedro", "pedro@email.com", "xyz", "33333333333")
        usuario = buscar_usuario("33333333333")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario['nome'], "Pedro")

    def test_deletar_usuario(self):
        criar_usuario("Ana", "ana@email.com", "pass", "44444444444")
        resultado = deletar_usuario("44444444444")
        self.assertEqual(resultado, "Usuário removido com sucesso.")
        self.assertEqual(len(usuarios), 2)

if __name__ == '__main__':
    unittest.main()