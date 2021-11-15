from contextlib import redirect_stdout #only for outputting debug to log file, may be deleted later
import numpy as np
import planetrips as va
import greedysol as greedy

def simulatedAnnealing(inst: va.Instance):
    

def main():
    instance = va.readInstance(1)
    solution = greedy.greedySolution(instance)
    print(instance.isFeasible(solution))

if __name__ == "__main__":
    main()

