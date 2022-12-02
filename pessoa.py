import json


def conferirID(tipoDePessoa):
    i = 0
    id = 0
    file = open('data.json')
    data = json.load(file)
    if tipoDePessoa == 'cliente':
        for pessoa in data['clientes']:
            i += 1
        id = i + 1
        return id
    elif tipoDePessoa == 'parceiros':
        for pessoa in data['parceiros']:
            i += 1
        id = i + 1
        return id

        
class Pessoa:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        
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
        entry = { "id": self.id, "nome": self.nome,"telefone" : self.telefone , "endereco": self.endereco,}
        data["clientes"].append(entry)
        with open('data.json', 'w') as file:
            json.dump(data, file)
        file.close()
        return 'Cliente Cadastrado'

    def CadastroParceiro(self, list):
        turno = {"manha" : False, "tarde" : False}
        entryParceiro = {"id": self.id , "nome": self.nome,"telefone" : self.telefone ,"servico": self.servico } 
        for semana in list:
            entryParceiro.update({semana : turno})
        file = open('data.json') #abre o arquivo JSON
        data = json.load(file) # variavel data carrega arquivo JSON para conseguir manipulá-lo em seguida
        data["parceiros"].append(entryParceiro) # chave "parceiros" do arquivo json 'data' vai receber por append a variável entryParceiro
        with open('data.json', 'w') as file: # abre o arquivo JSON no modo escrita
            # objeto python (data) tem que ser mantido em um arquivo JSON (file). json.dump escreve no arquivo e salva
            json.dump(data, file)
        file.close() #fecha o arquivo JSON
        return 'Parceiro Cadastrado'
    
    def CadastroServico(self):
        exist = False
        file = open('data.json') 
        data = json.load(file)
        entryServico = {"servico": self.servico} #entryServico recebe um objeto
        for key in data["servicos"]:
            if self.servico == key["servico"]:
                exist = True
            else:
                pass
        if exist == False:
            data["servicos"].append(entryServico) # chave "servicos" do arquivo json 'data' vai receber por append a variável entryServico
            with open('data.json', 'w') as file: #abre o arquivo JSON no modo escrita
                # objeto python (data) tem que ser mantido em um arquivo JSON (file). json.dump escreve no arquivo e salva
                json.dump(data, file)
        file.close() #fecha o arquivo JSON
        return 'Serviço Cadastrado'
    
    
        
