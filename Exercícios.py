#1. Seja uma lista de inteiros, mostre apenas os números pares usando list comprehension
lista = [-85, 12, 50, 39, -87, 25, 80, 34, 42]
[x for x in lista if x%2 == 0]

#2. Crie uma lista com os quadrados de todos os números pares de 1 a 20 usando list comprehension.
lista_quadrado = [x**2 for x in range(1,21) if x%2 == 0]

#3. Dada uma lista de palavras, ordene-a pelo tamanho das palavras em ordem crescente, utilizando sorted() com a cláusula key=.
palavras = ['espada', 'elfo', 'mago', 'cavaleiro', 'feiticeira', 'reino']
palavras.sort(key=len)

#4. Dada uma lista de palavras, ordene-a pelo número de vogais presentes em cada palavra.
palavras = ['espada', 'elfo', 'mago', 'cavaleiro', 'feiticeira', 'reino']

def contvogais(palavra):
    vogal = 'aeiou'
    cont = 0
    for p in palavra:
        if p.lower() in vogal:
            cont += 1
    return cont

palavras.sort(key=contvogais)

#5. Dada uma lista de palavras, ordene-a pelo último caractere de cada palavra
palavras = ['wotan', 'brunhilde', 'alberich', 'fricka', 'loge', 'fafner', 'donner']

def ultimo_caracter(palavra):
    return palavra[-1]

palavras.sort(key=ultimo_caracter)

#6. Dada uma string, utilize list comprehension para criar uma nova string onde os caracteres aparecem alternando entre maiúsculas e minúsculas.
palavra = 'tetraedro'
''.join([x.upper() if i%2 == 0 else x for i, x in enumerate(palavra)])

#7. Dada uma lista de strings contendo números misturados com letras (por exemplo, "a3b", "z12y", "c1x"), ordene a lista com base no número contido na string.
lista = ['a3b', 'z12y', 'c1x']

def encontra_nume(seq):
    resp = ''
    for c in seq:
        if c.isdigit():
            resp += c
    return(int(resp))

lista.sort(key=encontra_nume)

#8. Crie um dicionário que mapeia os números de 1 a 10 para seus respectivos quadrados, usando dict comprehension.
dicio = {n:n**2 for n in range(1,11)}

#9. Dada uma string, crie um dicionário onde as chaves são os caracteres e os valores são a contagem de vezes que cada caractere aparece.
palavra = 'paralelepipedo'
{x:palavra.count(x) for x in set(palavra)}

#10. Dado um dicionário qualquer, crie um novo dicionário onde as chaves e os valores estejam invertidos.
paises = {'EUA':'Washingtn', 'Alemanha':'Berlim', 'Japão':'Toquio', 'França':'Paris', 'Canada':'Otawa'}
{x:y for y, x in paises.items()}

#11. Dado um dicionário de números, crie um novo dicionário contendo apenas os pares chave-valor onde o valor seja maior que um determinado número.
numeros = {1:50, 2:30, 3:75, 4:28, 5:15, 6:70, 7:80, 8:12, 9:91, 10:2}
determinado_numero = 50
{k:v for k, v in numeros.items() if v > determinado_numero}

# 12. Dado um dicionário, ordene-o pelos valores.
numeros = {1:50, 2:30, 3:75, 4:28, 5:15, 6:70, 7:80, 8:12, 9:91, 10:2}
{k:v for k, v in sorted(numeros.items(), key=lambda item: item[1])}

# 13. Dado um dicionário onde as chaves são palavras, ordene-o com base no comprimento das chaves.
palavras = {"sol": 1, "cachorro": 2, "lua": 3, "computador": 4, "casa": 5, "floresta": 6, "amor": 7, "programacao": 8, "livro": 9, "amizade": 10}
{k:v for k, v in sorted(palavras.items(), key=lambda item: len(item[0]))}

# 14. Dada uma frase, crie um dicionário onde as chaves são palavras e os valores são a contagem de vezes que cada palavra aparece.
frase = 'O sol brilha e o sol aquece a terra, mas o sol também ilumina a noite.'.split()
{k:frase.count(k) for k in frase}

# 15. Dado um dicionário onde os valores são números, crie um novo dicionário onde cada valor seja a raiz quadrada do original.
