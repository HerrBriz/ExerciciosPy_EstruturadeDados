#1) Escreva uma função chamada maior_menor_que(lista, limite) que receba uma lista de números inteiros e um número limite. A função deve retornar o maior número da lista que seja menor que o limite. Se todos os elementos forem maiores ou iguais ao limite, retorne None. Não use sort ou max. Exemplo:
#maior_menor_que([10, 20, 30, 40], 35) → 30 e maior_menor_que([50, 60, 70], 40) → None.
def maior_menor_que(lista, limite):
  lista_nova = [n for n in lista if n < limite]
  if len(lista_nova) == 0:
    return None
  maior = lista_nova[0]
  for n in lista_nova[1:]:
    if n > maior:
      maior = n
  return maior


#2) Escreva uma função gato_atrapalha_sono(miando, hora, feriado) que recebe três argumentos: miando, que é True quando o gato está miando e False caso contrário; hora, um inteiro de 0 a 23 representando a hora do dia; e feriado, que é True se for feriado e False caso contrário.
#Considere que em dias normais o aluno dorme entre 21h e 5h, e em feriados entre 23h e 8h. A função deve retornar True se o gato estiver miando durante o horário de sono, atrapalhando o descanso do aluno. 
#Note que o gato miar exatamente na hora de acordar não atrapalha.
def gato_atrapalha_sono(miando, hora, feriado):
  if not miando:
    return False
  if feriado:
    return hora >= 23 or hora <= 8
  if not feriado:
    return hora >= 21 or hora <= 5


# 3) Escreva um programa que leia uma palavra por vez, digitada pelo usuário, até que ele digite "sair".
#Armazene as palavras em uma lista. Em seguida, imprima todas as palavras com mais de 5 letras e que contenham ao menos uma letra da palavra “python”. Suponha que todas as palavras estejam em letras minúsculas.
def pitonica(palavra):
    for p in palavra:
        if p.lower() in 'python':
            return True
            break
    return False

lista = []
while True:
    palavra = input()
    if palavra == 'sair':
        break
    else:
        lista.append(palavra)

for p in lista:
    if len(p) > 5 and pitonica(p):
        print(p)


#4) Escreva uma função válido(idade, renda) que recebe dois argumentos: a idade de uma pessoa (inteiro) e sua renda mensal (float ou inteiro).
#A função deve retornar True se a pessoa tiver 18 anos ou mais e renda de pelo menos R$2500, ou se tiver 21 anos ou mais, independentemente da renda. Caso contrário, a função deve retornar False.
def valido(idade, renda):
    if (idade >= 18 and renda >= 2500) or idade >= 21:
        return True
    else:
        return False


#5) O código abaixo foi escrito para somar os valores de uma lista de preços, mas contém vários erros distintos (de sintaxe e lógica).
#a) Encontre todos os erros, indicando se são de sintaxe ou de lógica.
#b) Reescreva o código corrigido.
def soma preços(lista):
    soma = 0.0
    for preço in lista:
        total = total + preço
        return total

preços = "19.90 35.00 12.50 9.90".split()
print = ("Total: R$" + soma preços(preços))

# 1° erro: Na definição da função, 'soma' e 'preço' devem estar juntos. O certo seria 'soma_preços' ou 'somapreços'.
# 2° erro: Na segunda linha a variável 'soma' é definida para iterar a soma, mas durante a iteração é usada a variável não declarada 'total'.
# 3° erro: 
