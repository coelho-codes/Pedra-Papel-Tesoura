from random import randint

def saudacoes():
    print('BEM VINDO(A) AO JOGO DE PEDRA, PAPEL E TESOURA!!')
    print('Para sair digite "sair" a qualquer momento.')
    print('================================================')

def logica(usuario, computador):
    #pedra -> 1, papel -> 2, tesoura -> 3
    if usuario == 'pedra' and computador == 1:
        print('Empate!') 
    elif usuario == 'pedra' and computador == 2:
        print('Você perdeu.') 
    elif usuario == 'pedra' and computador == 3:
        print('Parabéns, você ganhou!') 
    elif usuario == 'papel' and computador == 1:
        print('Parabéns, você ganhou!') 
    elif usuario == 'papel' and computador == 2:
        print('Empate!') 
    elif usuario == 'papel' and computador == 3:
        print('Você perdeu.') 
    elif usuario == 'tesoura' and computador == 1:
        print('Você perdeu.') 
    elif usuario == 'tesoura' and computador == 2:
        print('Parabéns, você ganhou!') 
    elif usuario == 'tesoura' and computador == 3:
        print('Empate!')
    else:
        print("Ops... Não entendi. Tente novamente.")

saudacoes()

ligado = True

while ligado:
    usuario = input('Escolha pedra, papel ou tesoura: ')
    computador = randint(1, 3)
    usuario.lower()

    if usuario == 'sair':
        print('Obrigado por jogar! :)')
        ligado = False
    else:
        logica(usuario, computador)