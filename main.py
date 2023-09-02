'''
---------------------------------------
Trabalho de APE - Batalha Naval
---------------------------------------
Programadores
---------------------------------------
Janderson Lima
João Paulo Azevedo
Fernando Julio 
Itallo Oliveira 
Adiel Sobral 
---------------------------------------
'''

import random as rd
import pickle
import time as tm

#inicia/zera algumas funcoes inciais
pontuacao = [0, 0]
qntd_barcos = 0
tabuleiro_jogador_gabarito = [[], []]
tabuleiro_jogador = [[], []]
nome1 = ''
nome2 = ''
jogador = None


#Função de iniciar o jogo
def iniciar_jogo():

    global tabuleiro_jogador
    global qntd_barcos
    global tabuleiro_jogador_gabarito
    global nome1
    global nome2
    global pontuacao
    global jogador

    #Verificar se o usuário quer continuar ou não
    #jogador quer começar do zero
    if not continuar == "s".upper():
        #Pedir número de barcos
        qntd_barcos = int(input('Digite a quantidade de barcos(1 a 6): '))

        #Manter barco dentro do range (1-6)
        if qntd_barcos < 1 or qntd_barcos > 6:
            print('Quantidade de barcos inválida, tente novamente. ')
            iniciar_jogo()
        print('')
        #Nomear jogadores
        nome1 = input('Digite o nome do jogador 1: ').upper()
        nome2 = input('Digite o nome de jogador 2: ').upper()
        #Gerando o tabuleiro com os navios
        tabuleiro_jogador_gabarito = [
            navios_tabuleiro(qntd_barcos),
            navios_tabuleiro(qntd_barcos)
        ]
        #Guardando o tabuleiro que será printado na tela e que é mutável de acordo com os tiros dos jogadores
        tabuleiro_jogador = [gerar_matriz(8), gerar_matriz(8)]
        jogador = 0
        #Consulta e carregamento de dados do "jogo carregado"

    #Busca dos dados do jogo carregado
    else:
        #retorna os dados salvos a cada chamado da variável
        pontuacao = jogo_carregado(pontuacao, qntd_barcos,
                                   tabuleiro_jogador_gabarito,
                                   tabuleiro_jogador, nome1, nome2, jogador)[0]
        qntd_barcos = jogo_carregado(pontuacao, qntd_barcos,
                                     tabuleiro_jogador_gabarito,
                                     tabuleiro_jogador, nome1, nome2,
                                     jogador)[1][0]

        tabuleiro_jogador_gabarito = jogo_carregado(
            pontuacao, qntd_barcos, tabuleiro_jogador_gabarito,
            tabuleiro_jogador, nome1, nome2, jogador)[2]
        tabuleiro_jogador = jogo_carregado(pontuacao, qntd_barcos,
                                           tabuleiro_jogador_gabarito,
                                           tabuleiro_jogador, nome1, nome2,
                                           jogador)[3]
        nome1 = jogo_carregado(pontuacao, qntd_barcos,
                               tabuleiro_jogador_gabarito, tabuleiro_jogador,
                               nome1, nome2, jogador)[4][0]
        nome2 = jogo_carregado(pontuacao, qntd_barcos,
                               tabuleiro_jogador_gabarito, tabuleiro_jogador,
                               nome1, nome2, jogador)[5][0]
        jogador = jogo_carregado(pontuacao, qntd_barcos,
                                 tabuleiro_jogador_gabarito, tabuleiro_jogador,
                                 nome1, nome2, jogador)[6]
        qntd_barcos = int(qntd_barcos)

    #Continuar o Jogo (verifica a qnt_barcos e pontuação)
    while pontuacao[0] != qntd_barcos and pontuacao[1] != qntd_barcos:

        #Personalização dos tabulerios com os nomes dos jogadores
        nome = ''
        if jogador == 0:
            nome = nome1
        else:
            nome = nome2

        nomeindex = ''
        if nome == nome1:
            nomeindex = nome2
        else:
            nomeindex = nome1

        outro_jogador = abs(jogador - 1)

        #print dos turnos e tabuleiros
        print(f'\n================= TURNO DE {nome} =================\n')

        print(f'     Tabuleiro de {nomeindex}:\n')
        gerar_matriz_print(tabuleiro_jogador[outro_jogador])

        print('\n', ' ' * 5 + 'Seu tabuleiro:\n')
        gerar_matriz_print(tabuleiro_jogador[jogador])

        #tiros
        tiro(tabuleiro_jogador[outro_jogador],
             tabuleiro_jogador_gabarito[outro_jogador], jogador)
        jogador = outro_jogador


#verifica quem ganhou
    if pontuacao[0] == qntd_barcos:

        print('\n', ' ' * 17, 'Fim de jogo!')
        print('\n', ' ' * 15, 'jogador 1 Venceu\n')

        print(f'             Pontuação do jogador 2: {pontuacao[1]}')

    else:
        print('\n', ' ' * 17, 'Fim de jogo!')
        print('\n', ' ' * 15, 'jogador 2 Venceu\n')

        print(f'             Pontuação do jogador 1: {pontuacao[0]}')

    print('\n============== Batalha Naval: O jogo ===============\n')


def teste_save():
    save(pontuacao, tabuleiro_jogador_gabarito, tabuleiro_jogador)
    print('\n', ' ' * 19 + 'JOGO SALVO!!\n')


#Função para requisitar coordenadas de ataque
def tiro(tabuleiro_atacar, tabuleiro_buscar, jogador):
    coordenadas = 'abcdefgh'

    #Solicitar coordenadas
    x = input(
        '\nDigite a coordenada da linha que deseja atacar(A-H): ').lower()
    if x == "save":
        teste_save()

    y = input('Digite a coordenada da coluna que deseja atacar(A-H): ').lower()
    if y == "save":
        teste_save()

    #Mostrar frotas
    if x == "dev" and y == "dev":
        print('\n', ' ' * 19 + 'Gabarito jogador 1:', "\n")
        gerar_matriz_print(tabuleiro_jogador_gabarito[0], )
        print('\n', ' ' * 19 + 'Gabarito jogador 2:', "\n")
        gerar_matriz_print(tabuleiro_jogador_gabarito[1], )
        x = input(
            '\nDigite a coordenada da linha que deseja atacar(A-H): ').lower()
        y = input(
            'Digite a coordenada da coluna que deseja atacar(A-H): ').lower()
    else:
        #Verifica se x e y é valido
        while x not in coordenadas:
            x = input("Escreva uma linha válida(ABCDEFGH): ")

        while y not in coordenadas:
            y = input("Escreva uma coluna válida(ABCDEFGH): ")

    #Transformando as coordenadas de letras para números
    xindex = coordenadas.find(x)
    yindex = coordenadas.find(y)

    #Verificando se o jogador já havia digitado as coordenadas anteriormente
    if tabuleiro_atacar[xindex][yindex] == "F" or tabuleiro_atacar[xindex][
            yindex] == "A":
        print('Local já selecionado, escolha novamente.')
        tiro(tabuleiro_atacar, tabuleiro_buscar, jogador)
    #Verificando se as coordenadas digitadas acertaram o navio
    else:
        if tabuleiro_buscar[xindex][yindex] == "N":
            print('\n', ' ' * 12 + 'FOGO! UM NAVIO FOI ATINGIDO.\n')
            tabuleiro_atacar[xindex][yindex] = 'F'
            pontuacao[jogador] += 1
            print(f'Pontuação atual: {pontuacao[jogador]}')
            print(f'Barcos restantes: {qntd_barcos - pontuacao[jogador]}')
            if pontuacao[jogador] != qntd_barcos:
                tiro(tabuleiro_atacar, tabuleiro_buscar, jogador)
    #Em caso de erro
        else:
            print('\n', ' ' * 19 + 'TIRO NA ÁGUA!\n')
            tabuleiro_atacar[xindex][yindex] = 'A'


#Gerador de matrizes para memória
def gerar_matriz(indice):
    matriz = [['~'] * indice for i in range(indice)]
    return matriz


#Gerador de matriz para print
def gerar_matriz_print(tabuleiro):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print("  ", end="")
    print('  '.join(letras))
    for i in range(8):
        print(letras[i], end=" ")
        print('  '.join(tabuleiro[i]))


#Colocar os barcos no tabuleiro
def navios_tabuleiro(qntd_barcos):
    matriz = [['~'] * 8 for i in range(8)]

    #Criação de variáveis para verificação
    posição_barcos = []
    posições_bloqueadas = []
    contadorbarcos = 0

    #Teste para verificar se todos os barcos já foram posicionados
    while contadorbarcos != qntd_barcos:
        linha_random = rd.randint(0, 7)
        coluna_random = rd.randint(0, 7)
        position = (linha_random, coluna_random)

        #Teste para verificar se o número aleatório gerado não diz respeito a uma célula que possui um navio ou células bloqueadas
        if position not in posições_bloqueadas and position not in posição_barcos:
            matriz[linha_random][coluna_random] = "N"
            contadorbarcos += 1
            posição_barcos.append(position)

            #Estrutura de repetição para armazenar as posições bloqueadas
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    else:
                        block_row = linha_random + x
                        block_column = coluna_random + y
                        posições_bloqueadas.append((block_row, block_column))
    return matriz


def save(pontuacao, tabuleiro_jogador_gabarito, tabuleiro_jogador):

    global dados

    #dados do programa
    dados = {
        'pontuacao jogador 1': pontuacao[0],
        'pontuacao jogador 2': pontuacao[1],
        'tabuleiro jogador gabarito 1': tabuleiro_jogador_gabarito[0],
        'tabuleiro jogador gabarito 2': tabuleiro_jogador_gabarito[1],
        'tabuleiro_jogador 1': tabuleiro_jogador[0],
        'tabuleiro_jogador 2': tabuleiro_jogador[1],
        'nome 1': nome1,
        'nome 2': nome2,
        'qntd_barcos': qntd_barcos
    }

    #salva o arquivo em PKL
    with open('jogo_salvo.pkl', 'wb') as arquivo:
        pickle.dump(dados, arquivo)


def jogo_carregado(pontuacao, qntd_barcos, tabuleiro_jogador_gabarito,
                   tabuleiro_jogador, nome1, nome2, jogador):

    #carrega os arquivos do jogo
    with open('jogo_salvo.pkl', 'rb') as arquivo:
        dados = pickle.load(arquivo)
    jogador = 0
    pontuacao = [dados['pontuacao jogador 1'], dados['pontuacao jogador 2']]
    qntd_barcos = [dados['qntd_barcos']]
    tabuleiro_jogador_gabarito = [
        dados['tabuleiro jogador gabarito 1'],
        dados['tabuleiro jogador gabarito 2']
    ]
    tabuleiro_jogador = [
        dados['tabuleiro_jogador 1'], dados['tabuleiro_jogador 2']
    ]
    nome1 = [dados['nome 1']]
    nome2 = [dados['nome 2']]
    #retorna os dados
    return pontuacao, qntd_barcos, tabuleiro_jogador_gabarito, tabuleiro_jogador, nome1, nome2, jogador


#Main Program

print('\n============== Batalha Naval: O jogo ===============\n')
print('Para salvar o jogo escreva "save" na linha ou coluna\n')

#Verificar se usuário quer continuar o jogo ou não

continuar = input("Deseja continuar o jogo?(S/N): ").upper()

if continuar == "S":
    iniciar_jogo()
else:
    pontuacao = [0, 0]
    iniciar_jogo()
