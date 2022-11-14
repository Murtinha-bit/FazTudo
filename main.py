import json

class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        
    def setServico(self, servico):
        self.servico = servico

    def getServico(self):
        return self.servico

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco

    def CadastroCliente(self):
        cliente = {}
        cliente[self.nome] = {'endereco' : self.endereco}
        with open('data.json', 'w') as file:
            json.dump(cliente, file)

pessoa = Pessoa(input('Digite o nome da pessoa: '))
pessoa.setEndereco('Sao Joao Batista')
pessoa.CadastroCliente()
