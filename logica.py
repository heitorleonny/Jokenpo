from time import sleep
import random

import self as self


class Jokenpo():

    def __init__(self):
    # lista de opções

    lista_de_opcoes = ['papel', 'tesoura', 'pedra']
    pc = 0
    jogador = 0


    #placar


    # escolha do pc


    def escolha_pc(lista_de_opcoes):
        opcao_pc = random.choice(lista_de_opcoes)
        return opcao_pc


    #escolha do jogador


    def escolha_jogador():
        print('Digite o número de acordo com sua escolha')
        sleep(1)
        print('1 PAPEL')
        sleep(1)
        print('2 TESOURA')
        sleep(1)
        print('3 PEDRA')
        sleep(1)
        p = True
        while p is True:
            opcao_jogaor = int(input('Sua escolha:'))
            if opcao_jogaor != 1 and opcao_jogaor != 2 and opcao_jogaor !=3:
                p = True
            else:
                p = False
        return opcao_jogaor

    #comparação


    def comparacao():
        pc = 0
        jogador = 0
        opcao_pc = escolha_pc()
        opcao_jogador = escolha_jogador()
        if opcao_pc == 'papel':
            if opcao_jogador == 1:
                print('TIVEMOS UM EMPATE! AMBOS ESCOLHERAM PAPEL')
                sleep(1)
            elif opcao_jogador == 2:
                print('VOCÊ VENCEU A RODADA! TESOURA GANHA DE PAPEL')
                sleep(1)
            elif opcao_jogador == 3:
                print('VOCÊ PERDEU A RODADA! PEDRA PERDE PARA PAPEL')
                sleep(1)


        elif opcao_pc == 'tesoura':
            if opcao_jogador == 1:
                print('VOCÊ PERDEU A RODADA! TESOURA GANHA DE PAPEL')
                sleep(1)
            elif opcao_jogador == 2:
                print('TIVEMOS UM EMPATE! AMBOS ESCOLHERAM TESOURA')
                sleep(1)
            elif opcao_jogador == 3:
                print('VOCÊ GANHOU A RODADA! PEDRA GANHA PARA TESOURA')
                sleep(1)

        elif opcao_pc == 'pedra':
            if opcao_jogador == 1:
                print('VOCÊ GANHOU A RODADA! PAPEL GANHA DE PEDRA')
                sleep(1)
            elif opcao_jogador == 2:
                print('VOCÊ PERDEU A RODADA! PEDRA GANHA DE TESOURA')
                sleep(1)
            elif opcao_jogador == 3:
                print('TIVEMOS UM EMPATE AQUI! AMBOS ESCOLHERAM PEDRA')
                sleep(1)

        # pontuacao
        if opcao_pc == 'papel' and opcao_jogador == 3 or opcao_pc == 'tesoura' and opcao_jogador == 1 or opcao_pc == 'pedra' and opcao_jogador == 2:
            pc += 1
        elif opcao_pc == 'papel' and opcao_jogador == 2 or opcao_pc == 'tesoura' and opcao_jogador == 3 or opcao_pc == 'pedra' and opcao_jogador == 1:
            jogador += 1

        print('O PLACAR ESTÁ ASSIM:')
        sleep(1)
        print('PC:', pc)
        print('VOCÊ', jogador)


    def mensagem_inicial():
        sleep(1)
        print('OLÁ, SEJA BEM VINDO!')
        sleep(2)
        print('VOCÊ ESTÁ PRESTES A INICIAR UMA PARTIDA DE JOKENPO CONTRA O PC')
        sleep(2)
        print('VENCE AQUELE QUE ATINGIR DOIS PONTOS PRIMEIRO')
        sleep(2)
        print('BOA SORTE!')




    #chamada pro jogo

    def run():

        mensagem_inicial()
        jogando = True
        pc = 0
        jogador = 0
        while jogando is True:
            if pc == 2:
                print('O JOGO ACABOU E O VENCEDOR FOI O PC')
                print('PLACAR FINAL:')
                sleep(1)
                print('PC:', pc)
                print('VOCÊ', jogador)
                jogando = False
            if jogador == 2:
                print('O JOGO ACABOU! VOCÊ VENCEU')
                print('PLACAR FINAL:')
                sleep(1)
                print('PC:', pc)
                print('VOCÊ', jogador)
                jogando = False
            comparacao()

