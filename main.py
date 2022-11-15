import json
from pessoa import *

def diasDeTrabalho():
    list = [] 
    continueInput = 's'
    while continueInput == 's' or semana != 8:
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
                continueInput = input('Deseja cadastrar mais um dia? (S/N)').lower()
    return list

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
        list = diasDeTrabalho()
        parceiro.CadastroParceiro(list)

    case 3: 
        print('3')
    case 4: 
        print('4')


