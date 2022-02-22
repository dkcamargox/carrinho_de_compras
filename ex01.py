
def check_palavra(palavra_analisada):
    for palavra in palavras:
        if palavra_analisada == palavra:
            continue
        letras_check = 0
        for letra in palavra_analisada:
            if letra in palavra:
                letras_check += 1
        if (letras_check == len(palavra_analisada)):
            print(f'{palavra_analisada} pode ser escrita com as letras de {palavra}\n')

palavras = []
for i in range(5):
    palavras.append(input('insira uma palavra:\t'))


for palavra in palavras:
    check_palavra(palavra)