import planetrips as va
from solution import Solution

def greedySolution(inst : va.Instance): #finds an initial greedy solution that will be optimized with simulated annealing
    availableSpace = inst.PCapacity.tolist()
    availablePeople = list(range(inst.nPeople))
    sol = Solution(inst)
    sortedPlanes = list(range(inst.kPlanes))
    sortedPlanes.sort(key = lambda x:availableSpace[x])
    for plane in sortedPlanes:
        person = max(availablePeople,
                           key=lambda x:inst.cIndividual[x]/inst.pWeights[x], default = -1)
        if person != -1 and inst.pWeights[person] <= availableSpace[plane]:
            sol.allocate(person, plane)
            availableSpace[plane] -= inst.pWeights[person]
            availablePeople.remove(person)
            planeHasSpace = True
            while(planeHasSpace):
                friend = max(availablePeople,
                                   key=lambda x:((inst.cIndividual[x] + inst.cPair[person][x])\
                                   /inst.pWeights[x]) * (x!=person), default = -1)
                if friend != -1 and inst.pWeights[friend] <= availableSpace[plane]:
                    sol.allocate(friend, plane)
                    availableSpace[plane] -= inst.pWeights[friend]
                    availablePeople.remove(friend)
                else:
                    planeHasSpace = False
    return sol
