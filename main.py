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
        file = open('data.json') #abre o arquivo JSON
        data = json.load(file) # variavel data carrega arquivo JSON para conseguir manipulá-lo em seguida
        entryParceiro = { "nome": self.nome,"servico": self.servico} # cria objeto que pega nome e serviço do parceiro e atribui a variável entryParceiro
        data["parceiros"].append(entryParceiro) # chave "parceiros" do arquivo json 'data' vai receber por append a variável entryParceiro
        with open('data.json', 'w') as file: # abre o arquivo JSON no modo escrita
            # objeto python (data) tem que ser mantido em um arquivo JSON (file). json.dump escreve no arquivo e salva
            json.dump(data, file)
        entryServico = {"servico": self.servico} #entryServico recebe um objeto
        data["servicos"].append(entryServico) # chave "servicos" do arquivo json 'data' vai receber por append a variável entryServico
        with open('data.json', 'w') as file: #abre o arquivo JSON no modo escrita
            # objeto python (data) tem que ser mantido em um arquivo JSON (file). json.dump escreve no arquivo e salva
            json.dump(data, file)
        file.close() #fecha o arquivo JSON

escolha = 0
print('Faz tudo WEB \n')
escolha = int(input('1 - Cadastro Cliente \n2 - Cadastro Parceiro \n3 - Financeiro \n4 - Solicitar Servico \n'))
match escolha:
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


