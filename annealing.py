import random
import copy
import planetrips as va
from utils import greedySolution
from utils import randomSolution
from solution import Solution
import numpy as np

def flipCoin(prob: float): #returns the result of a coin flip (true or false) with probability equals prob
    return random.random() < prob

def calcInitialTemp(instance : va.Instance): 
    solution_values = []
    for _ in range(20):
        solution_values.append(randomSolution(instance).value)
    return max(solution_values) - min(solution_values)


def calcIParameter(inst: va.Instance): #calculates the I parameter, following the given specifications.
    return inst.nPeople * inst.kPlanes 

def metropolis(solution : Solution, temperature : float, iterations : int):
    best = copy.copy(solution)
    for _ in range(iterations):
        candidate = copy.copy(solution)
        candidate.randomNeighbourStep()
        delta = candidate.value - solution.value
        if delta > 0:
            solution = copy.copy(candidate)
            if solution.value > best.value:
                best = copy.copy(solution)
        elif delta < 0:
            accept_prob = np.exp(delta/temperature)
            if flipCoin(accept_prob):
                solution = copy.copy(candidate)
    return best

def simulatedAnnealing(instance: va.Instance, min_temperature : float, cooling_rate : float, k : int): 
    temperature = calcInitialTemp(instance)
    I = calcIParameter(instance) #number of iterations without changing the temp value.
    solution = greedySolution(instance)

    while (temperature > min_temperature):
        for _ in range(I):
            candidate = metropolis(solution, temperature, k)
            if candidate.value - solution.value > 0:
                solution = copy.copy(candidate)
        temperature *= cooling_rate #updates the temperature
    return solution
    

def main():
    instance = va.readInstance(1)
    greedy = greedySolution(instance)
    random = randomSolution(instance)
    initialTemp = calcInitialTemp(instance)
    print("Greedy solution: ", greedy.value)
    print("Random solution: ", random.value)
    print("Initial temperature: ", initialTemp)
    new_solution = simulatedAnnealing(instance, 100, 0.9, 500)
    print("Annealed value: ", new_solution.value)
    print("Feasible?: ", new_solution.isFeasible())
if __name__ == "__main__":
    main()

