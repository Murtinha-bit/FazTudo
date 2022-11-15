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

    def CadastroParceiro(self, list):
        turno = {"manha" : False, "tarde" : False}
        entryParceiro = { "nome": self.nome,"servico": self.servico}
        for semana in list:
            entryParceiro.update({semana : turno})
        file = open('data.json') #abre o arquivo JSON
        data = json.load(file) # variavel data carrega arquivo JSON para conseguir manipulá-lo em seguida
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