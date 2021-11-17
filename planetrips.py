import numpy as np
import os

class Instance:
    def __init__(self, nPeople : int, kPlanes : int, cIndividual : np.ndarray,
                 cPair : np.ndarray, pWeights : np.ndarray):
        self.nPeople = nPeople
        self.kPlanes = kPlanes
        self.cIndividual = cIndividual
        self.cPair = cPair
        self.pWeights = pWeights
        self.PCapacity = self.__calculatePlaneCapacity(pWeights, kPlanes)

    def __calculatePlaneCapacity(self, pWeights : np.ndarray, kPlanes : int): #calculates a plane capacity following the given description.
        planeCapacity = np.zeros(kPlanes)
        totalWeight = np.sum(pWeights)
        for k in range(kPlanes):
            planeCapacity[k] = 0.8 * (totalWeight/(kPlanes))
        return planeCapacity

    def __str__(self):
        return f"""
        {self.nPeople=}
        {self.kPlanes=}
        {self.cIndividual.size=}
        {self.cPair.size=}
        {self.pWeights.size=}
        {self.PCapacity.size=}
        """

def readInstance(input_file : str, test = False): #reads instances from input file. 

    if not os.path.isfile(input_file):
        raise Exception("Invalid input file")
    file = open(input_file, 'r')

    nPeople = int(file.readline()) #first line is n
    cIndividual = np.fromiter(map(int, file.readline().split()), int) #second line is c vector

    cPair = np.zeros((nPeople, nPeople)) 
    for i in range(nPeople - 1):  
        lineRead = np.fromiter(map(int, file.readline().split()), int)
        for j in range(lineRead.size):
            cPair[i][i+j+1] = lineRead[j] #next lines are matrix c, i in [n-1], j in [i+1,n]
            cPair[i+j+1][i] = lineRead[j]
    
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
