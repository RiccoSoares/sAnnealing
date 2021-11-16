import math
import random
import copy
import planetrips as va
from greedysol import greedySolution
from solution import Solution
import numpy as np
MIN_TEMPERATURE = 1
COOLING_RATE = 0.8

def flipCoin(prob: float): #returns the result of a coin flip (true or false) with probability equals prob
    return random.random() < prob

def calcInitialTemp(inst: va.Instance): #calculates the initial temp for the algorithm, following the given specifications.
    #not implemented yet
    return 1000000

def calcIParameter(inst: va.Instance): #calculates the I parameter, following the given specifications.
    return inst.nPeople 

def metropolis(solution : Solution, temperature : float, iterations : int):
    best = copy.copy(solution)
    for _ in range(iterations):
        candidate = copy.copy(solution)
        candidate.randomNeighbourStep()
        delta = candidate.value - solution.value
        if delta > 0:
            solution = copy.copy(candidate)
        elif delta < 0:
            accept_prob = np.exp(delta/temperature)
            if flipCoin(accept_prob):
                solution = copy.copy(candidate)
    return max(best, solution, key=lambda x:x.value) 

def simulatedAnnealing(inst: va.Instance): #inst arg represents an initial solution given by greedy algorithm.
    temp = calcInitialTemp(inst)
    current = greedySolution(inst)
    candidate = copy.copy(current)

    I = calcIParameter(inst) #corresponds to the number of iterations without changing the temp value.
    while (temp > MIN_TEMPERATURE):
        for _ in range(I):
            candidate = metropolis(current, temp, 100)
            candidate.randomNeighbourStep()
            delta = candidate.value - current.value
            if delta > 0:
                current = copy.copy(candidate)
        temp *= COOLING_RATE #updates the temperature
    return current
    

def main():
    instance = va.readInstance(1)
    greedy = greedySolution(instance)
    print("Initial solution: ", greedy.value)
    new_solution = simulatedAnnealing(instance)
    print("New value: ", new_solution.value)

if __name__ == "__main__":
    main()

