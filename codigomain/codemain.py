#  Jogo jokenpo - v1.0.0.3
"""
v1.0.0.3 - Atualizações:
- texto sobre quatidade de partidas.
- inclusão da animação sleep para inicio da jogada.
"""

from random import randint
from time import sleep
import emoji
import pygame

#  lógica do jogo para somatória
jogadas = 0
vit_jogador = 0
empate = 0
vit_cpu = 0
encerrar = ' '
design = 15

#  inicio do código principal
while encerrar != 'N':
    itens = ('Pedra', 'Papel', 'Tesoura')
    cpu = randint(0, 2)
    print('''\nJOGADOR ESCOLHA SUA JOGADA...
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
''')
    print(f'''{jogadas}ª Partida(s)...
<< Placar >>
Jogador: {vit_jogador}
Empates: {empate}
Computador: {vit_cpu}
    ''')
    jogador = int(input('Escolha sua jogada: '))
    sleep(0.3)
    print('JOGADA INICIADA', end='')
    for cont_ponto in range (3):
        sleep(0.8)
        print('.', end='')
    print('')
    if jogador < 3:
        jogadas += 1
        print('-=' * design)
        print('Computador jogou: {}' .format(itens[cpu]))
        print('Jogador escolheu: {}' .format(itens[jogador]))
    if cpu == 0:  # Computador joga pedra.
        if jogador == 0:
            print('Jogada Emptada!')
            print('-=' * design)
            empate += 1
        elif jogador == 1:
            print('Jogador é o vencedor!')
            print('-=' * design)
            vit_jogador += 1
        elif jogador == 2:
            print('Computador é o vencedor!')
            print('-=' * design)
            vit_cpu += 1
        else:
            print('Jogada inválida.')
            print('-=' * design)
    elif cpu == 1:  # Computador joga papel.
        if jogador == 0:
            print('Computador é o vencedor!')
            print('-=' * design)
            vit_cpu += 1
        elif jogador == 1:
            print('Jogada Empatada!')
            print('-=' * design)
            empate += 1
        elif jogador == 2:
            print('Jogador é o vencedor!')
            print('-=' * design)
            vit_jogador += 1
        else:
            print('Jogada inválida.')
            print('-=' * design)
    elif cpu == 2:  # Computador joga tesoura.
        if jogador == 0:
            print('Jogador é o Vencedor!')
            print('-=' * design)
            vit_jogador += 1
        elif jogador == 1:
            print('Computador é o vencedor!')
            print('-=' * design)
            vit_cpu += 1
        elif jogador == 2:
            print('Jogada Empatada!')
            print('-=' * design)
            empate += 1
        else:
            print('Jogada inválida.')
            print('-=' * design)
    encerrar = str(input('\nDesejar continuar jogando [S/N]? ')).upper().strip()[0]
print('')
print('-=' * design)
print('FIM DO JOGO!')
print(f'''JOGADAS {jogadas}
<< Placar Final >>
Jogador: {vit_jogador}
Empates: {empate}
Computador: {vit_cpu}
''')
print('-=' * design)
