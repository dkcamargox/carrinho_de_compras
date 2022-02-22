

def check_palavra(palavra_analisada, palavra):
    letras_check = 0    
    for letra in palavra_analisada:
        
        if letra in palavra:
            letras_check += 1
            
    if (letras_check == len(palavra_analisada)):
        return True
    else:
        return False

def check_palavras(palavra1, palavra2):
    if(check_palavra(palavra2, palavra1) and check_palavra(palavra1, palavra2)):
        return True
    else:
        return False

palavra1=input('digite a palavra 1:')
palavra2=input('digite a palavra 2:')
print(check_palavras(palavra1, palavra2))