import planetrips as va
from solution import Solution

def greedySolution(inst : va.Instance): #finds an initial greedy solution that will be optimized with simulated annealing
    availablePeople = list(range(inst.nPeople))
    sol = Solution(inst)
    for plane in range(inst.kPlanes):
        person = max(availablePeople,
                           key=lambda x:inst.cIndividual[x]/inst.pWeights[x], default = -1)
        if person != -1 and inst.pWeights[person] <= sol.freeSpace[plane]:
            sol.allocate(person, plane)
            sol.freeSpace[plane] -= inst.pWeights[person]
            availablePeople.remove(person)
            planeHasSpace = True
            while(planeHasSpace):
                friend = max(availablePeople,
                                   key=lambda x:((inst.cIndividual[x] + inst.cPair[person][x])\
                                   /inst.pWeights[x]) * (x!=person), default = -1)
                if friend != -1 and inst.pWeights[friend] <= sol.freeSpace[plane]:
                    sol.allocate(friend, plane)
                    sol.freeSpace[plane] -= inst.pWeights[friend]
                    availablePeople.remove(friend)
                else:
                    planeHasSpace = False
    return sol
