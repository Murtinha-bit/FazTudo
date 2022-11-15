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
        semana = []
        entrysemana = {"manha" : False, "tarde" : False}
        semana.append(entrysemana)
        file = open('data.json') #abre o arquivo JSON
        data = json.load(file) # variavel data carrega arquivo JSON para conseguir manipulá-lo em seguida
        entryParceiro = { "nome": self.nome,"servico": self.servico, "segunda" : semana , "terca" : semana , 
        "quarta" : semana , "quinta" : semana , "sexta" : semana , "sabado" : semana , "domingo" : semana } # cria objeto que pega nome e serviço do parceiro e atribui a variável entryParceiro
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
        list = []
        continueInput = 's'
        parceiro = Pessoa(input('Digite o seu nome: '), True)
        parceiro.setServico(input('Digite o servico que voce quer prestar :'))
        while continueInput == 's' or semana == 8:
            print("Digite os dias da semana que voce quer trabalhar:")
            semana = input("1 - SEGUNDA\n 2 - TERCA\n 3 - QUARTA\n 4 - QUINTA\n 5 - SEXTA\n 6 - SABADO\n 7 - DOMINGO\n 8 - TODOS")
            match semana:
                case 1:
                    list.append('segunda')
                case 2:
                    list.append('terca')
                case 3:
                    list.append('quarta')
                case 4:
                    list.append('quinta')
                case 5:
                    list.append('sexta')
                case 6:
                    list.append('sabado')
                case 7:
                    list.append('domingo')
                case 8:
                    list.append('segunda')
                    list.append('terca')
                    list.append('quarta')
                    list.append('quinta')
                    list.append('sexta')
                    list.append('sabado')
                    list.append('domingo')
            continueInput = input('Deseja cadastrar mais um dia? (S/N)').lower()
            
        file = open('data.json')
        parceiro.CadastroParceiro()
    case 3: 
        print('3')
    case 4: 
        print('4')


