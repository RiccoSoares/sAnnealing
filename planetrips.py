import numpy as np
import random
#from contextlib import redirect_stdout #only for outputting debug to log file, may be deleted later

class Solution:
    def __init__(self, kPlanes : int, nPeople : int):
        self.vMatrix = np.zeros((kPlanes, nPeople))

    def allocate(self, person, plane):
        self.vMatrix[plane][person] = 1
        
    def deAllocate(self, person, plane):
        self.vMatrix[plane][person] = 0
        
    def getAllocation(self, person, plane):
        return self.vMatrix[plane][person]
        
    def invAllocation(self, person, plane):
        if self.getAllocation(person, plane):
            self.deAllocate(person, plane)
        else:
            self.allocate(person, plane)

    def __str__(self):
        return str(self.vMatrix)
        

class Instance:
    def __init__(self, nPeople : int, kPlanes : int, cIndividual : np.ndarray,
                 cPair : np.ndarray, pWeights : np.ndarray):
        self.nPeople = nPeople
        self.kPlanes = kPlanes
        self.cIndividual = cIndividual
        self.cPair = cPair
        self.pWeights = pWeights
        self.PCapacity = self.calculatePlaneCapacity(pWeights, kPlanes)

    def calculatePlaneCapacity(self, pWeights : np.ndarray, kPlanes : int): #calculates a plane capacity following the given description.
        planeCapacity = np.zeros(kPlanes)
        totalWeight = np.sum(pWeights)
        for k in range(kPlanes):
            planeCapacity[k] = 0.8 * (totalWeight/(k+1))
        return planeCapacity

    def isFeasible(self, sol : Solution): #determines wether or not a solution is feasible
        planesPerPerson = sol.vMatrix.sum(axis=0) 

        #sum of planes per person is bool, only one or zero
        onePlanePerPerson = np.array_equal(planesPerPerson, planesPerPerson.astype(bool))
        if not onePlanePerPerson:
            return False
        plane = 0
        for row in sol.vMatrix:
            planeWeight = 0
            for person in range(self.nPeople):
                planeWeight += row[person]*self.pWeights[person]
                if planeWeight > self.PCapacity[plane]:
                    return False    
            plane += 1

        return True
        
    def evaluateSolution(self, sol : Solution): #returns the profit assured by given solution or -1 in case the solution is not feasible.
        if self.isFeasible(sol):
            val = 0
            
            for plane in range(self.kPlanes):
                for person in range(self.nPeople):
                    if (sol.getAllocation(person, plane)):  #if the person is allocated to the plane
                        val += self.cIndividual[person]
                        
                    for anotherPerson in range(self.nPeople):
                        if (sol.getAllocation(anotherPerson, plane)):
                            val += self.cPair[person][anotherPerson]
                    
            return val
        else:
            return -1
            
    def returnNeighbour(self, sol : Solution): #returns a random neighbour from given solution.
        plane = random.choice(range(self.kPlanes))
        person = random.choice(range(self.nPeople))
        sol.invAllocation(person, plane)
        
        return sol
                     
    def __str__(self):
        return f"""
        {self.nPeople=}
        {self.kPlanes=}
        {self.cIndividual.size=}
        {self.cPair.size=}
        {self.pWeights.size=}
        {self.PCapacity.size=}
        """


def readInstance(nInstance : int): #reads instances from input file. 
    filename = f'data/VA{nInstance:02d}.dat'
    file = open(filename, 'r')

    nPeople = int(file.readline()) #first line is n
    cIndividual = np.fromiter(map(int, file.readline().split()), int) #second line is c vector

    cPair = np.zeros((nPeople, nPeople)) 
    for i in range(nPeople - 1):  
        lineRead = np.fromiter(map(int, file.readline().split()), int)
        for j in range(lineRead.size):
            cPair[i][i+j+1] = lineRead[j] #next lines are matrix c, i in [n-1], j in [i+1,n]
            cPair[i+j+1][i] = lineRead[j]

    """
    Prints cPair matrix to log file for debug purposes
    TODO: delete this portion as soon as cPair's content is consistenly tested

    np.set_printoptions(linewidth=100000, threshold=10000)
    with open('cPairLog.txt', 'w') as f: 
        with redirect_stdout(f):
            print(cPair)
    """
    
    for i in range(3):      # 3 lines of nothing, according to input file's description.
        file.readline()

    pWeights = np.fromiter(map(int, file.readline().split()), int) # last line is the weights

    if (nPeople - 1)%3 == 0:
        kPlanes = 3
    elif (nPeople - 1)%3 == 1:
        kPlanes = 5
    elif (nPeople - 1)%3 == 2:
        kPlanes = 10
    else:
        kPlanes = -1

    return Instance(nPeople, kPlanes, cIndividual, cPair, pWeights) 
