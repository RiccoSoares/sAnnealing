import numpy as np
from contextlib import redirect_stdout

class problemInstance:
    def __init__(self, nPeople : int, kPlanes : int, cIndividual : np.ndarray,
                 cPair : np.ndarray, pWeights : np.ndarray):
        self.nPeople = nPeople
        self.kPlanes = kPlanes
        self.cIndividual = cIndividual
        self.cPair = cPair
        self.pWeights = pWeights
        self.PCapacity = self.calculatePlaneCapacity(pWeights, kPlanes)

    def calculatePlaneCapacity(self, pWeights : np.ndarray, kPlanes : int):
        planeCapacity = np.zeros(kPlanes)
        totalWeight = np.sum(pWeights)
        for k in range(kPlanes):
            planeCapacity[k] = 0.8 * (totalWeight/(k+1))
        return planeCapacity

    def __str__(self):
        return f"""
        {self.nPeople=}
        {self.kPlanes=}
        {self.cIndividual.size=}
        {self.cPair.size=}
        {self.pWeights.size=}
        {self.PCapacity.size=}"""


def readProblemInstance(nInstance : int):
    filename = f'va_instances/VA{nInstance:02d}.dat'
    file = open(filename, 'r')

    nPeople = int(file.readline()) #first line is n
    cIndividual = np.fromiter(map(int, file.readline().split()), int) #second line is c vector

    cPair = np.zeros((nPeople, nPeople))
    for i in range(nPeople - 1):  # n - 1 lines of matrix c
        lineRead = np.fromiter(map(int, file.readline().split()), int)
        for j in range(lineRead.size):
            cPair[i][i+j+1] = lineRead[j]
            cPair[i+j+1][i] = lineRead[j]

    np.set_printoptions(linewidth=100000, threshold=10000)
    with open('out.txt', 'w') as f:
        with redirect_stdout(f):
            print(cPair)
    
    for i in range(3):      # 3 lines of nothing
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

    return problemInstance(nPeople, kPlanes, cIndividual, cPair, pWeights) 

def main():

    print(readProblemInstance(1))

if __name__ == "__main__":
    main()
        

