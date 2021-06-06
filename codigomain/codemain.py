#  Jogo jokenpó - v1.0.0.1

from random import randint
from time import sleep
import emoji
import pygame

#  comandos do jogo
jogadas = 0
vit_jogador = 0
empate = 0
vit_cpu = 0
encerrar = ' '
desing = 15

while encerrar != 'N':
    itens = ('Pedra', 'Papel', 'Tesoura')
    cpu = randint(0, 2)
    print('''\nJOGADOR ESCOLHA SUA JOGADA...
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
''')
    print(f'''Jogada de número: {jogadas}
<< Placar >>
Jogador: {vit_jogador}
Empates: {empate}
Computador: {vit_cpu}
    ''')
    jogador = int(input('Escolha sua jogada: '))
    if jogador < 3:
        jogadas += 1
        print('-=' * desing)
        print('Computador jogou: {}' .format(itens[cpu]))
        print('Jogador escolheu: {}' .format(itens[jogador]))
    if cpu == 0:  # Computador joga pedra.
        if jogador == 0:
            print('Jogada Emptada!')
            print('-=' * desing)
            empate += 1
        elif jogador == 1:
            print('Jogador é o vencedor!')
            print('-=' * desing)
            vit_jogador += 1
        elif jogador == 2:
            print('Computador é o vencedor!')
            print('-=' * desing)
            vit_cpu += 1
        else:
            print('Jogada inválida.')
            print('-=' * desing)
    elif cpu == 1:  # Computador joga papel.
        if jogador == 0:
            print('Computador é o vencedor!')
            print('-=' * desing)
            vit_cpu += 1
        elif jogador == 1:
            print('Jogada Empatada!')
            print('-=' * desing)
            empate += 1
        elif jogador == 2:
            print('Jogador é o vencedor!')
            print('-=' * desing)
            vit_jogador += 1
        else:
            print('Jogada inválida.')
            print('-=' * desing)
    elif cpu == 2:  # Computador joga tesoura.
        if jogador == 0:
            print('Jogador é o Vencedor!')
            print('-=' * desing)
            vit_jogador += 1
        elif jogador == 1:
            print('Computador é o vencedor!')
            print('-=' * desing)
            vit_cpu += 1
        elif jogador == 2:
            print('Jogada Empatada!')
            print('-=' * desing)
            empate += 1
        else:
            print('Jogada inválida.')
            print('-=' * desing)
    encerrar = str(input('\nDesejar continuar jogando [S/N]? ')).upper().strip()[0]
print('')
print('-=' * desing)
print('FIM DO JOGO!')
print(f'''JOGADAS {jogadas}
<< Placar Final >>
Jogador: {vit_jogador}
Empates: {empate}
Computador: {vit_cpu}
''')
print('-=' * desing)
