import os

PRODUCT_LIST = []


TOTAL_VALUE = 0.0

# carrega os produtos de dentro do arquivo
def load_products_data():
    return [
        { 'description':'BONECA', 'price':'300', 'code':'1'},
        { 'description':'CARRINHO', 'price':'500', 'code':'2'},
        { 'description':'BOLA', 'price':'200', 'code':'3'}
    ]


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


# faz a compra do produto e pergunta continuar ou terminar
def buy(product_code):
    global TOTAL_VALUE
    TOTAL_VALUE = TOTAL_VALUE + float(search_product(product_code)['price'])
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

