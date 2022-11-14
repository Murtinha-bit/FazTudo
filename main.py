import json

class Pessoa:

    def __init__(self, nome, cliente):
        self.nome = nome
        self.cliente = cliente
        
    def setServico(self, servico):
        self.servico = servico

    def getServico(self):
        return self.servico

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco

    def CadastroCliente(self):
        file = open('data.json')
        data = json.load(file)
        entry = { "nome": self.nome,"endereco": self.endereco, "id": self.id}
        data["clientes"].append(entry)
        with open('data.json', 'w') as file:
            json.dump(data, file)
        file.close()

    def CadastroParceiro(self):
        file = open('data.json')
        data = json.load(file)
        entryParceiro = { "nome": self.nome,"servico": self.servico}
        data["parceiros"].append(entryParceiro)
        with open('data.json', 'w') as file:
            json.dump(data, file)
        entryServico = {"servico": self.servico}
        data["servicos"].append(entryServico)
        with open('data.json', 'w') as file:
            json.dump(data, file)
        file.close()

escolha = 0
print('Faz tudo WEB \n')
escolha= int(input('1 - Cadastro Cliente \n2 - Cadastro Parceiro \n3 - Financeiro \n4 - Solicitar Servico \n'))
match escolha :
    case 1:
        contador = 1
        cliente = Pessoa(input('Digite o seu nome: '), True)
        cliente.setEndereco(input('Digite o endereco :'))
        file = open('data.json')
        data = json.load(file)
        while contador > 0:
            contador = 0
            id = (int(input('Digite seu id (Sera usado para logar no seu usuario depois): ')))
            for key in data["clientes"]:
                if id == key["id"]:
                    contador=+1
            if contador > 0:
                print('Esse id ja existe para outro usuario, por favor escolha outro: ')
        cliente.setId(id)
        cliente.CadastroCliente()
    case 2: 
        parceiro = Pessoa(input('Digite o seu nome: '), True)
        parceiro.setServico(input('Digite o servico que voce quer prestar :'))
        file = open('data.json')
        parceiro.CadastroParceiro()
    case 3: 
        print('3')
    case 4: 
        print('4')


