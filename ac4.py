"""
Programação Estruturada

12/09/2023
AC4
"""

#01. Elabore uma função e_primo(num) que retorna se um número num é primo ou não. Caso num não seja primo, liste todos os números pelos quais num é divisível.

def e_primo(num):
    primo = True
    for div in range(2, num):
        if num % div == 0:
            print('{} não é um número primo. É divisível por: {}'.format(num, div))
            primo = False
    
    return primo

numero = 17
resultado = e_primo(numero)

if resultado:
    print('{} é um número primo.'.format(numero))


#02. Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento. O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas, e o percentual de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo. O relatório com as opções de pagamento deve conter os seguintes dados: valor dos juros, valor total da dívida (incluindo juros), quantidade de parcelas e valor da parcela. A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido. No momento, não é necessário formatar os valores.

def mostrar_parcelamento(divida)
    print('Não consegui pensar um jeito de fazer essa aqui professor')


#03. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

def contar_numeros_por_intervalo():
    intervalos = [0, 0, 0, 0]

    while True:
        numero = int(input('Digite um número positivo (ou um negativo para encerrar o programa): '))
        
        if numero < 0:
            break
        
        if 0 <= numero <= 25:
            intervalos[0] += 1
        elif 26 <= numero <= 50:
            intervalos[1] += 1
        elif 51 <= numero <= 75:
            intervalos[2] += 1
        elif 76 <= numero <= 100:
            intervalos[3] += 1

    return intervalos

def imprimir_contagem(intervalos):
    print('Quantidade de números nos intervalos:')
    print('[0-25]:', intervalos[0])
    print('[26-50]:', intervalos[1])
    print('[51-75]:', intervalos[2])
    print('[76-100]:', intervalos[3])

intervalos = contar_numeros_por_intervalo()
imprimir_contagem(intervalos)