import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')



def pedir_palpite(letras_escritas):   
    palpite = str(input('\nQual o seu palpite ? ')).strip()
 # While criado para evitar erros
    while palpite in letras_escritas or len(palpite) > 1 or len(palpite) == 0 or palpite.isdigit():
        if palpite in letras_escritas:
     
            print('Essa letra já foi escrita, por favor tente novamente!')
            palpite = str(input('\n\nQual o seu palpite ? ')) 
     
        elif len(palpite) > 1 or len(palpite) == 0:
         
            print('Por favor, escreva apenas uma letra')
            palpite = str(input('\n\nQual o seu palpite ? ')) 
        elif palpite.isdigit() == True:
     
            print('Isso não é uma letra, por favor digite apenas letras.')
            palpite = str(input('\n\nQual o seu palpite ? ')) 
            
    return palpite



def mostrar_palavras_descobertas(manu = ' '):
    for i in manu:
        print(i, end=' ')


def animacao():
    print('-=' * 30)
    print('                        JOGO DA FORCA')
    print('-=' * 30)
    
    print('Bem Vindo ao jogo da forca!!! ')


def preparar_palavra(word, discovered_letters): 
    for i in word:
        if i != ' ':
            discovered_letters.append('_')
        else:
            discovered_letters.append('-')
            acertos+=1

