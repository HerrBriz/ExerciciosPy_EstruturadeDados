#Escreva uma função chamada maior_menor_que(lista, limite) que receba uma lista de números inteiros e um número limite. A função deve retornar o maior número da lista que seja menor que o limite. Se todos os elementos forem maiores ou iguais ao limite, retorne None. Não use sort ou max. Exemplo:
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


#Escreva uma função gato_atrapalha_sono(miando, hora, feriado) que recebe três argumentos: miando, que é True quando o gato está miando e False caso contrário; hora, um inteiro de 0 a 23 representando a hora do dia; e feriado, que é True se for feriado e False caso contrário.
#Considere que em dias normais o aluno dorme entre 21h e 5h, e em feriados entre 23h e 8h. A função deve retornar True se o gato estiver miando durante o horário de sono, atrapalhando o descanso do aluno. 
#Note que o gato miar exatamente na hora de acordar não atrapalha.
def gato_atrapalha_sono(miando, hora, feriado):
  if not miando:
    return False
  if feriado:
    return hora >= 23 or hora <= 8
  if not feriado:
    return hora >= 21 or hora <= 5
