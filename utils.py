import planetrips as va
from solution import Solution

def greedySolution(inst : va.Instance): #finds an initial greedy solution that will be optimized with simulated annealing
    availablePeople = list(range(inst.nPeople))
    solution = Solution(inst)
    for plane in range(inst.kPlanes):

        person = max(availablePeople,
                           key=lambda x:inst.cIndividual[x]/inst.pWeights[x], default = -1)
        #returns person with biggest value/weight ratio, or -1 if there is no person available

        if person != -1 and inst.pWeights[person] <= solution.freeSpace[plane]:
            #if person fits in plane, allocate them, else go to next plane
            solution.vMatrix[plane][person] = 1
            solution.freeSpace[plane] -= inst.pWeights[person]
            availablePeople.remove(person)
            planeHasSpace = True
            while(planeHasSpace):
                friend = max(availablePeople,
                                   key=lambda x:((inst.cIndividual[x] + inst.cPair[person][x])\
                                   /inst.pWeights[x]) * (x!=person), default = -1)
                #return friend with biggest value/weight ratio, or -1 if there is no person available
                if friend != -1 and inst.pWeights[friend] <= solution.freeSpace[plane]:
                    #if friend fits, allocate them, else go to next plane
                    solution.vMatrix[plane][friend] = 1
                    solution.freeSpace[plane] -= inst.pWeights[friend]
                    availablePeople.remove(friend)
                else:
                    planeHasSpace = False
    solution.value = solution.evaluate()
    return solution

