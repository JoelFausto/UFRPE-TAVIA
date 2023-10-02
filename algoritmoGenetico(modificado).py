import random
import config
from cromossomo import Cromossomo
from population import Population
import plot

def algoritmoGenetico_PM():

    print('-------------------------------------------------------------')
    print("Knapsack Problem (Problema da Mochila) - Algoritmo Genético")
    print("                   UFRPE 2023 - TAvIA                      ")
    print('-------------------------------------------------------------')
    print()

    # armazena o histórico de gerações
    cronologia = []

    # inicializa uma população aletoriamente
    populacao = Population()
    populacao.initialize()
    populacao.evaluate()

    print(f"População Inicial")
    populacao.print()

    cronologia.append(populacao)

    # executa as rodadas de sucessivas gerações
    for p in range(config.generations-1):

        # gera uma nova população baseada no antecessor
        novaPop = Population()
        novaPop.procreate(cronologia[-1])
        novaPop.evaluate()

        print(f"População {p + 1}")
        novaPop.print()

        cronologia.append(novaPop)

    melhor = cronologia[-1].cromossomos[0]

    # Tentativa de minimizar o espaço vazio
    c = Cromossomo()
    esp_sob = melhor.knapsackCapacity - melhor.weight
    cont = 0
    for i in melhor.composition:
        # print(i, c.available_itens_weight[cont], esp_sob)
        if c.available_itens_weight[cont] <= esp_sob:
            maior = c.available_itens_weight[cont]
            if c.available_itens_weight[cont] > maior:
                melhor.composition[i] = 1
        esp_sob = melhor.knapsackCapacity - melhor.weight
        cont += 1

    print('-------------------------------------------------------------')
    print("Knapsack Problem (Problema da mochila) - Algoritmo Genético")
    print('-------------------------------------------------------------')
    print("A melhor resposta encontrada foi:")
    print(f"Composição: {melhor.composition}")
    print(f"Valor: {melhor.value}")
    print(f"Peso: {melhor.weight} ")
    print('-------------------------------------------------------------')

    return melhor

algoritmoGenetico_PM()