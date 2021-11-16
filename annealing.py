import numpy as np
import math
import random
import planetrips as va
import greedysol as greedy
from sty import fg,bg
MIN_TEMPERATURE = 0.01
COOLING_RATE = 0.8

def flipCoin(prob: float): #returns the result of a coin flip (true or false) with probability equals prob
    
    return random.random() > prob

def calcInitialTemp(inst: va.Instance): #calculates the initial temp for the algorithm, following the given specifications.
    #not implemented yet
    
    return 1

def calcIParameter(inst: va.Instance): #calculates the I parameter, following the given specifications.
    
    return inst.nPeople * inst.kPlanes

def simulatedAnnealing(inst: va.Instance): #inst arg represents an initial solution given by greedy algorithm.
    temp = calcInitialTemp
    current_sol = inst
    I = calcIParameter(inst) #corresponds to the number of iterations without changing the temp value.
    
    while (temp > MIN_TEMPERATURE):
        for i in range(I):
            current_eval = va.valuateSolution(current_sol)
            candidate = va.returnNeighbour(current_sol)
            candidate_eval = va.evaluateSolution(candidate)
            delta = candidate_eval - current_eval
            
            if delta > 0:
                current_sol = candidate
            else:
                accept_prob = pow(math.e, delta/temp)
                if flipCoin(accept_prob):
                    current_sol = candidate
        
        temp = temp*COOLING_RATE #updates the temperature
    
    return current_sol
    

def main():
    instance = va.readInstance(1)
    solution = greedy.greedySolution(instance)
    np.set_printoptions(linewidth=2000)
    print(solution.vMatrix)
    while(True):
        print()
        print(bg.black + fg.green + (str(solution.vMatrix)))
        solution.randomNeighbourStep()
    """
    print("Initial solution is feasable: ", solution.isFeasible())
    print("Initial solution value: ", solution.value)
    solution.randomNeighbourStep()
    print("New Solution is feasable: ", solution.isFeasible())
    print("New Solution value: ", solution.value)
    #new_solution = simulatedAnnealing(solution)
    #print(instance.isFeasible(new_solution))
    """

if __name__ == "__main__":
    main()

