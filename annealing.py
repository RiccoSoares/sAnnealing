import math
import random
from copy import deepcopy
import planetrips as va
from greedysol import greedySolution
import numpy as np
MIN_TEMPERATURE = 10
COOLING_RATE = 0.8

def flipCoin(prob: float): #returns the result of a coin flip (true or false) with probability equals prob
    return random.random() > prob

def calcInitialTemp(inst: va.Instance): #calculates the initial temp for the algorithm, following the given specifications.
    #not implemented yet
    return 100000

def calcIParameter(inst: va.Instance): #calculates the I parameter, following the given specifications.
    return inst.nPeople * inst.kPlanes 


def simulatedAnnealing(inst: va.Instance): #inst arg represents an initial solution given by greedy algorithm.
    temp = calcInitialTemp(inst)
    current = greedySolution(inst)
    candidate = deepcopy(current)

    I = calcIParameter(inst) #corresponds to the number of iterations without changing the temp value.
    while (temp > MIN_TEMPERATURE):
        for _ in range(I):
            current = deepcopy(candidate)
            candidate.randomNeighbourStep()
            delta = candidate.value - current.value
            if delta > 0:
                current = deepcopy(candidate)
            elif delta < 0:
                accept_prob = pow(math.e,-delta/temp)
                if flipCoin(accept_prob):
                    current = deepcopy(candidate)
        temp = temp*COOLING_RATE #updates the temperature
    return current
    

def main():
    instance = va.readInstance(4, test = True)
    greedy = greedySolution(instance)
    print("Initial solution is feasable: ", greedy.isFeasible())
    print("Initial solution value: ", greedy.value)
    #new_solution = simulatedAnnealing(solution)
    #print(instance.isFeasible(new_solution))

if __name__ == "__main__":
    main()

