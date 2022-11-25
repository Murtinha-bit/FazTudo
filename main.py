import json
from pessoa import *
from semana import *






escolha = 0
print('Faz tudo WEB \n')
escolha = int(input('1 - Cadastro Cliente \n2 - Cadastro Parceiro \n3 - Financeiro \n4 - Solicitar Servico \n'))
match escolha:
    #######################################################################
    case 1:
        tipoDePessoa = 'cliente'
        cliente = Pessoa(input('Digite o seu nome: '),input('Digite o seu numero de telefone :'))
        cliente.setEndereco(input('Digite o endereco :'))
        file = open('data.json')
        data = json.load(file)
        id = conferirID(tipoDePessoa)
        cliente.setId(id)
        cliente.CadastroCliente()
    #######################################################################
    case 2: 
        tipoDePessoa = 'parceiros'
        parceiro = Pessoa(input('Digite o seu nome: ') ,input('Digite o seu numero de telefone :'))
        parceiro.setServico(input('Digite o servico que voce quer prestar :'))
        list = diasDeTrabalho()
        id = conferirID(tipoDePessoa)
        parceiro.setId(id)
        parceiro.CadastroParceiro(list)
        parceiro.CadastroServico()

    #######################################################################
    case 3: 
        print('3')

    #######################################################################
    case 4: 
        cont = 0
        file = open('data.json')
        data = json.load(file)
        print('Escolha o servico desejado com base na lista abaixo: ')
        for key in data['servicos']:
            cont = cont + 1
        for i in range(cont):
            print('\n '+ str(i) + ' - ' + data['servicos'][i]['servico'] )
        escolhaServico = int(input(''))
        semana = pegarSemana()
        print('\nPara qual turno do dia voce deseja?')
        turno = int(input('1 - manha \n2 - tarde \n'))
        match turno:
            case 1:
                turno = 'manha'
            case 2:
                turno = 'tarde'
        cont = 0
        empty = True
        print('Selecione uns de nossos parceiros disponiveis (Digite o numero na frente do nome do parceiro): \n')
        for pessoa in data['parceiros']:
            cont = cont + 1
            if pessoa['servico'] == data['servicos'][escolhaServico]['servico'] :
                if semana in pessoa:
                    if pessoa[semana][turno] == False:
                        print(str(pessoa['id']) + ' - ' + pessoa['nome'] + '\n')
                        empty = False
        if empty == False:
            escolhaParceiro = int(input(''))
            for i in range(cont):
                if data['parceiros'][i]['id'] == escolhaParceiro:
                    print('\nParabens o match esta feito, ja mandamos suas informacoes para nosso parceiro')
                    print('e aqui esta o numero dele para entrar em contato: ' + data['parceiros'][i]['telefone'])
                    data['parceiros'][i][semana][turno] = (True)   
            with open('data.json', 'w') as file:
                json.dump(data, file)
            file.close() 
        else:
            print('Desculpe mas nao temos parceiros disponiveis nessa data, faca outra solicitacao pf')
        
        


