import os

PRODUCT_LIST = []


TOTAL_VALUE = 0.0


CSV_FILE = 'data.csv'

# carrega os produtos de dentro do arquivo
def load_products_data():
    global CSV_FILE
    products = []
    with open(CSV_FILE, 'r') as file:
        lines = []
        for line in file:
                data = line.split(';')
                # busca pelo \n para apagarlo
                for index, string in enumerate(data):
                    if '\n' in string:
                        data[index] = string[:len(string)-1]
                # cada linda do csv num vetor
                lines.append(data)
        # bota tudo num array de dict
        for index, line in enumerate(lines):
            if index == 0:
                continue
            
            products.append({
                f'{lines[0][0]}': f'{line[0]}',
                f'{lines[0][1]}': f'{line[1]}',
                f'{lines[0][2]}': f'{line[2]}'
            })
    return products


# escreve continuar ou finalizar e le o resultado
def print_buy_menu():
    print('\t\tADICIONADO AO CARRINHO')
    print('\t\tC) CONTINUAR COMPRAS')
    print('\t\tF) FINALIZAR COMPRAS')
    return input()


# busca produtos de dentro da lista
def search_product(product_code):
    for product in PRODUCT_LIST:
        if product['code'] == f'{product_code}':
            return product


def quantity_menu():
    while(1):
        print('\t\tINSIRA A QUANTIDADE:')
        try:
            return int(input('\t\tQUANTIDADE:\t'))
        except:
            input('POR FAVOR INSERIR UM VALOR VÁLIDO')
            os.system('cls')
            continue

# faz a compra do produto e pergunta continuar ou terminar
def buy(product_code):
    
    global TOTAL_VALUE
    TOTAL_VALUE = TOTAL_VALUE + (float(search_product(product_code)['price']) * quantity_menu())
    os.system('cls')
    while(1):
        choice = print_buy_menu()
        if(choice.upper() == 'C'):
            break
        elif(choice.upper() == 'F'):
            break
        else:
            input('Opção invalida!')
            os.system('cls')
            continue
    return choice.upper() == 'C'


# escreve os produtos na tela
def print_product_list():
    print('\t\t\tPRODUTOS')
    print(f'\t\t0)  VOLTAR')
    for product in PRODUCT_LIST:
        this_product_description = product['description'].upper()
        this_product_code = product['code']
        print(f'\t\t{this_product_code})  {this_product_description}')
    return input()


# lida com a inserção do menu de produtos
def print_product_list_menu():
    # TODO
    while(1):
        choice = print_product_list()
        try:
            choice = int(choice)
        except:
            input('POR FAVOR INSERIR UM VALOR VÁLIDO')
            os.system('cls')
            continue
        if choice != 0:
            os.system('cls')
            continue_buying = buy(choice)
            os.system('cls')
            if(continue_buying):
                continue
            else:
                return os.system('cls')
        elif choice == 0:
            return os.system('cls')


# escreve o menu principal
def print_mainmenu():
    print('\t\t\tMAIN MENU')
    print('\t\tA) MOSTRAR PRODUTOS')
    print('\t\tB) SAIR')
    return input((''))


# escreve a tela final com o valor total
def print_final_screen():
    global TOTAL_VALUE
    print('\t\tVOCÊ ENCERROU AS COMPRAS')
    print(f'\t\tSEU PEDIDO DEU O DEU O VALOR TOTAL DE: R${round(TOTAL_VALUE, 2):.2f}')
    return input()


def main():
    while(1):
        choice = print_mainmenu()
        os.system('cls')
        if choice.upper() == 'A':
            print_product_list_menu()
            os.system('cls')
            return print_final_screen()

        elif choice.upper() == 'B':
            return

        else:
            input('Opção invalida!')
            os.system('cls')



if __name__ == '__main__':
    PRODUCT_LIST = load_products_data()
    os.system('cls')
    main()
    os.system('cls')

