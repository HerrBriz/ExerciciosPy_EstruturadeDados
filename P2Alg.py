#1) Escreva uma função maior_abaixo_media(lista) que receba uma lista de números inteiros e devolva o maior número da lista, que seja menor que a média dos elementos.
#Resolva o problema em duas etapas: a) Calcule a média dos valores e crie uma nova lista apenas com os elementos menores que a média. b) Retorne o maior valor dessa nova lista. Se não houver nenhum valor menor que a média, a função deve retornar None. Não use as funções sort, max, nem bibliotecas.
#Apenas para o cálculo da média você pode usar sum e len. Exemplos: maior_abaixo_media([10, 20, 30, 40]) -> 20, maior_abaixo_media([5, 5, 5]) -> None, maior_abaixo_media([1, 100]) -> 1, maior_abaixo_media([4, -8, 15, -16, 23, 42]) -> 4


#2) Crie uma função zigue_zague(s) que, dada uma string s, transforme em maiúsculas as letras que estiverem em posições ímpares. Exemplos: zigue_zague('abacate') -> 'aBaCaTe', zigue_zague('') -> ''


#3) O código abaixo foi escrito para somar os valores de uma lista de preços, mas contém vários erros distintos (de sintaxe e lógica). a) Encontre todos os erros. b) Reescreva o código corrigido.
def soma(lista):
    soma = 0.0
    for p in lista:
        total = total + p
    return total

precos = "19.90 35.00 12.50 9.90".split()
print ("Total: R$" + soma(precos))

#4) Defina pares_finais(n). A função recebe um número inteiro positivo n. Ela deve retornar quantos dígitos pares aparecem seguidos no final do número. Exemplos: pares_finais(245680) -> 3, pares_finais(123456) -> 1, pares_finais(13) -> 0.
