import json


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