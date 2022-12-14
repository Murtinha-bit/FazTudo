from pessoa import *
import unittest

class TestPessoa(unittest.TestCase):
    def teste_getServico(self):
        self.pessoa = Pessoa('Gabriela', '3199999')
        self.pessoa.setServico('Desenvolvedora')
        resultado = self.pessoa.getServico()
        esperado = 'Desenvolvedora'
        self.assertEqual(resultado, esperado)

    def teste_getId(self):
        self.pessoa = Pessoa('Murta', '3199999')
        self.pessoa.setId('Desenvolvedor')
        resultado = self.pessoa.getId()
        esperado = 'Desenvolvedor'
        self.assertEqual(resultado, esperado)
    
    def teste_getEndereco(self):
        self.pessoa = Pessoa('Murta', '3199999')
        self.pessoa.setEndereco('Rua Teste 123')
        resultado = self.pessoa.getEndereco()
        esperado = 'Rua Teste 123'
        self.assertEqual(resultado, esperado)

    def teste_cadastroCliente(self):
        cliente = Pessoa('Felipe Stemler', '99999999')
        cliente.setEndereco('Rua abcd')
        cliente.setId(99);
        resultado = cliente.CadastroCliente()
        esperado = 'Cliente Cadastrado'
        self.assertEqual(resultado, esperado)

        
    def teste_cadastroParceiro(self):
        parceiro = Pessoa('Murtinha do Python', '99999999')
        parceiro.setServico('Programador Python')
        parceiro.setId(35);
        list = ['segunda', 'quarta']
        resultado = parceiro.CadastroParceiro(list)
        esperado = 'Parceiro Cadastrado'
        self.assertEqual(resultado, esperado)


unittest.main(argv=[''], verbosity=2, exit=False)