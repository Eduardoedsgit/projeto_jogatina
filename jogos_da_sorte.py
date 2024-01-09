'''
Título: Jogos da sorte
Programa mega sena, loto mania e bixo
Autor: Eduardo Machado de Souza
projeto iniciado em 17/08/2023
'''
#A bilbioteca importada random serve para a máquina escolher um número aleatório
import random;
#importando a biblioteca de teampo
import time;

#comando para quebra de linha
print('\n');
#comando para imprimir 42 vezes o caractere ~ 
print(42*'~');
mensagem_jogo = ' Jogos da Sorte '
print('{:^42}'.format(mensagem_jogo));


print(42*'~');
print('Digite um dos números para escolher o jogo:\n',
        '1 - > Mega Sena\n',
        '2 - > Quina\n',
        '3 - > Jogo do Bixo\n',
        '4 - > Loto mania\n',
        '5 - > Loto Fácil\n',
        '6 - > Tome Mania\n',
        '7 - > Bingo'
        );
#lendo a entrada para a variável menu do tipo int(inteiro)
menu = int(input('Digite: '))
#comando match (corresponder) corresponde aos casos, ideal para riar menus de escolhas.
match menu:
    case 1:
        print(62* '~')
        print('                    Bem vindo a Mega Sena!')
        #define o número aleatorio pelo método random e randint é do tipo inteiro.
        #variável criada de nome aleatorio onde vai de 1 á 60 (1, 60);
        aleatorio = random.randint(1, 60);
        print('                    Cartela da mega Sena')
        print(62*'~');
        print('Você pode jogar marcando em um, dois ou nos três quadros abaixo')
        print('     [01] [02] [03] [04] [05] [06] [07] [08] [09] [10]\n',
              '    [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]\n',
              '    [21] [22] [23] [24] [25] [26] [27] [28] [29] [30]\n',
              '    [31] [32] [33] [34] [35] [36] [37] [38] [39] [40]\n',
              '    [41] [42] [43] [44] [45] [46] [47] [48] [49] [50]\n',
              '    [51] [52] [53] [54] [55] [56] [57] [58] [59] [60]');
        print(62*'~')

        #criando uma variável do tipo lista
        lista_jogador = list()
        #guarda o valor digitado na variável lista
        #append (acrescentar) vai adicionar oque será digitado na variável lista.
        lista_jogador.append(int(input('Digite o primeiro número escolhido na cartela: ')))
        #mostra na tela o número digitado da cartela do jogo
        print('[{}]'.format(lista_jogador[0]));
        #guarda o segundo valor na variável lista.
        lista_jogador.append(int(input('Digite o segundo número escolhido na lista: ')))
        #mostra os dois dígitos escolhidos na cartela
        print('[{}] [{}]'.format(lista_jogador[0], lista_jogador[1])); 
        lista_jogador.append(int(input('Digite o terceiro valor escolhido na cartela: ')))
        #mostra na tela os 3 números digitados na cartela 
        print('[{}] [{}] [{}]'.format(lista_jogador[0], lista_jogador[1], lista_jogador[2]))
        lista_jogador.append(int(input('Digite o quarto número escolhido na cartela: ')));
        print('[{}] [{}] [{}] [{}]'.format(lista_jogador[0], lista_jogador[1], lista_jogador[2], lista_jogador[3]));
        lista_jogador.append(int(input('Digite o quinto número escolhido na cartela: ')));
        print('[{}] [{}] [{}] [{}] [{}]'.format(lista_jogador[0], lista_jogador[1], lista_jogador[2], lista_jogador[3], lista_jogador[4])); 
        lista_jogador.append(int(input('Digite o sexto número escolhido na cartela: ')));
        print('[{}] [{}] [{}] [{}] [{}] [{}]'.format(lista_jogador[0], lista_jogador[1], lista_jogador[2], lista_jogador[3], lista_jogador[4], lista_jogador[5]));
        #cria uma variável de lista para guardar os números sorteados.
        numeros_sorteados = list();
        #comando random(aleatório) onde a máquina vai escolher um número aleatório de 1 a 60.
        #randint significa números inteiros e adc o número na variavel numeros aleatorios
        numeros_aleatorios = random.randint(1, 60);
        #adc o número aleatório na variável lista chamada numeros_sorteados
        #o comando append(acrescentar) acrescenta o valor na lista e do tipo int(inteiro).
        numeros_sorteados.append(int(numeros_aleatorios));
        numeros_aleatorios = random.randint(1, 60);
        numeros_sorteados.append(int(numeros_aleatorios));
        numeros_aleatorios = random.randint(1, 60);
        numeros_sorteados.append(int(numeros_aleatorios));
        numeros_aleatorios = random.randint(1, 60);
        numeros_sorteados.append(int(numeros_aleatorios));
        numeros_aleatorios = random.randint(1, 60);
        numeros_sorteados.append(int(numeros_aleatorios));
        numeros_aleatorios = random.randint(1, 60);
        numeros_sorteados.append(int(numeros_aleatorios));
        #quebra de linha
        print('\n');
        print(62*'~');
        print('       Atenção para os números sorteados!');
        print('          [{}] [{}] [{}] [{}] [{}] [{}]'.format(numeros_sorteados[0], numeros_sorteados[1], numeros_sorteados[2], numeros_sorteados[3], numeros_sorteados[4], numeros_sorteados[5]));
        print(62*'~');
        print('       Números que você escolheu na cartela')
        print('            [{}] [{}] [{}] [{}] [{}] [{}]'.format(lista_jogador[0], lista_jogador[1], lista_jogador[2], lista_jogador[3], lista_jogador[4], lista_jogador[5]));
        print(62*'~');        
            
    case 2:
        print('Bem vindo a Quina!');
        print(62*'~');
    case 3:
        print('Bem vindo ao jogo do Bixo');
        print(42*'~');
    case 4:
        print('Bem vindo ao Loto Mania!');
        print(42*'~');
    case 5:
        print('Bem vindo ao Loto Fácil!');
        print(42*'~');
    case 6:
        print('Bem vindo ao Loto Mania');
        print(42*'~');
    case 7:
        print('Bem vindo ao Bingo!');
        print(42*'~');
    case _:
        print('Digite O menu Correto!!!');
      



