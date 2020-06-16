from time import sleep
from telas.entrada_de_dados import mostrar_palavras_descobertas
from telas import entrada_de_dados
from telas.mostra_forca import mostrar_forca
from telas.entrada_de_dados import animacao
from telas.entrada_de_dados import preparar_palavra , clear


clear()

animacao()

palavra = str(input('Digite a palavra a ser descoberta: ')).strip().lower()
letras_descobertas = list()
letras_escritas = []
tentativas = 0
acertos = 0



mostrar_forca(tentativas)
preparar_palavra(palavra, letras_descobertas)

clear()

while acertos != len(palavra) or tentativas != 6:

    if acertos == len(palavra):
        clear()
        print(f'Parabéns, você venceu !\n\nA palavra era "{palavra.title()}"')
        break

    elif tentativas == 6:
        mostrar_forca(tentativas)

        print(f'\nVocê perdeu !!\nA palavra certa era "{palavra.title()}" ')
        sleep(1)
        break
    print(f'Letras já escritas: {letras_escritas}\n\n')

    mostrar_forca(tentativas) 
    mostrar_palavras_descobertas(letras_descobertas)
    palpite =entrada_de_dados.pedir_palpite(letras_escritas)
    letras_escritas.append(palpite)
    palpite.lower()


    if palpite in palavra:
        if palavra.count(palpite) > 1:

            positionPalpite = palavra.index(palpite)
            letras_Repetidas_Descobertas = 0

            while letras_Repetidas_Descobertas < palavra.count(palpite):
                # A váriavel position primeiro procura a posição do palpite da pessoa na lista
                # Quando ele achar a posição ele vai somar com o tamanho da lista, de 0 ate a posição do palpite

                position = palavra[positionPalpite:].index(palpite) + len(palavra[0:positionPalpite])
                
                if letras_descobertas[position] == '_':
                 	letras_Repetidas_Descobertas += 1
                 	acertos+=1

                # Adiciona o palpite a lista.

                letras_descobertas[position] = palpite
               
                # Aqui ele adiciona mais 1 a variavel positionPalpite, para que ele procure a próxima posição.
                
                positionPalpite += 1
   
        else:
            acertos+=1
            letras_descobertas[palavra.index(palpite)] = palpite
    else:
        tentativas+=1
    clear()