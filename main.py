import json
from pessoa import *

def diasDeTrabalho():
    list = [] 
    continueInput = 's'
    while continueInput == 's':
            escolhido = 0
            print("Digite os dias da semana que voce quer trabalhar:")
            semana = int(input("1 - SEGUNDA\n2 - TERCA\n3 - QUARTA\n4 - QUINTA\n5 - SEXTA\n6 - SABADO\n7 - DOMINGO\n8 - TODOS\n"))
            match semana:
                case 1:
                    for item in list:
                        print(item)
                        if 'segunda' == item:
                            escolhido = 1
                        else:
                            pass
                    if escolhido == 0 :
                        list.append('segunda')
                    else:
                        print('Voce ja escolheu esse dia da semana, escolha um dia diferente')
                case 2:
                    for item in list:
                        if 'terca' == item:
                            escolhido = 1
                        else:
                            pass
                    if escolhido == 0 :
                        list.append('terca')
                    else:
                        print('Voce ja escolheu esse dia da semana, escolha um dia diferente')
                case 3:
                    for item in list:
                        if 'quarta' == item:
                            escolhido = 1
                        else:
                            pass
                    if escolhido == 0 :
                        list.append('quarta')
                    else:
                        print('Voce ja escolheu esse dia da semana, escolha um dia diferente')
                case 4:
                    for item in list:
                        if 'quinta' == item:
                            escolhido = 1
                        else:
                            pass
                    if escolhido == 0 :
                        list.append('quinta')
                    else:
                        print('Voce ja escolheu esse dia da semana, escolha um dia diferente')
                case 5:
                    for item in list:
                        if 'sexta' == item:
                            escolhido = 1
                        else:
                            pass
                    if escolhido == 0 :
                        list.append('sexta')
                    else:
                        print('Voce ja escolheu esse dia da semana, escolha um dia diferente')
                case 6:
                    for item in list:
                        if 'sabado' == item:
                            escolhido = 1
                        else:
                            pass
                    if escolhido == 0 :
                        list.append('sabado')
                    else:
                        print('Voce ja escolheu esse dia da semana, escolha um dia diferente')
                case 7:
                    for item in list:
                        if 'domingo' == item:
                            escolhido = 1
                        else:
                            pass
                    if escolhido == 0 :
                        list.append('domingo')
                    else:
                        print('Voce ja escolheu esse dia da semana, escolha um dia diferente')
                case 8:
                    list.append('segunda')
                    list.append('terca')
                    list.append('quarta')
                    list.append('quinta')
                    list.append('sexta')
                    list.append('sabado')
                    list.append('domingo')
                    continueInput = 'n'
            if semana != 8 : 
                continueInput = input('Deseja cadastrar mais um dia? (S/N) \n').lower()
    return list

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

def pegarSemana():
    print('\nPara qual dia da semana voce necessita o servico?\n')
    semana = int(input('1 - segunda \n2 - terca \n3 - quarta \n4 - quinta \n5 - sexta\n6 - sabado \n7 - domingo\n'))
    match semana:
        case 1:
            return 'segunda'
        case 2:
            return 'terca'
        case 3:
            return 'quarta'
        case 4:
            return 'quinta'
        case 5:
            return 'sexta'
        case 6:
            return 'sabado'
        case 7:
            return 'domingo'
        
   
    





escolha = 0
print('Faz tudo WEB \n')
escolha = int(input('1 - Cadastro Cliente \n2 - Cadastro Parceiro \n3 - Financeiro \n4 - Solicitar Servico \n'))
match escolha:
    case 1:
        tipoDePessoa = 'cliente'
        cliente = Pessoa(input('Digite o seu nome: '),input('Digite o seu numero de telefone :'))
        cliente.setEndereco(input('Digite o endereco :'))
        file = open('data.json')
        data = json.load(file)
        id = conferirID(tipoDePessoa)
        cliente.setId(id)
        cliente.CadastroCliente()
    case 2: 
        tipoDePessoa = 'parceiros'
        parceiro = Pessoa(input('Digite o seu nome: ') ,input('Digite o seu numero de telefone :'))
        parceiro.setServico(input('Digite o servico que voce quer prestar :'))
        list = diasDeTrabalho()
        id = conferirID(tipoDePessoa)
        parceiro.setId(id)
        parceiro.CadastroParceiro(list)
        parceiro.CadastroServico()

    case 3: 
        print('3')
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
                        # escolhaParceiro = int(input(str(pessoa['id']) + ' - ' + pessoa['nome'] + '\n'))
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
        
        


