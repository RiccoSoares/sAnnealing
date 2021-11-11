class problemInstance:
    def __init__(self, nPeople : int, kPlanes : int, cIndividual : list[int],
                 cPair : list[list[int]], pWeights : list[int]):
        self.nPeople = nPeople
        self.kPlanes = kPlanes
        self.cIndividual = cIndividual
        self.cPair = cPair
        self.pWeights = pWeights
        self.PCapacity = self.calculatePlaneCapacity(pWeights, kPlanes)

    def calculatePlaneCapacity(self, pWeights : list[int], kPlanes : int):
        planeCapacity = [None] * kPlanes
        totalWeight = sum(pWeights)
        for k in range(kPlanes):
            planeCapacity[k] = 0.8 * (totalWeight/(k+1))
        return planeCapacity

    def __str__(self):
        return f"""
        {self.nPeople=}
        {self.kPlanes=}
        {len(self.cIndividual)=}
        {len(self.cPair)=}
        {len(self.pWeights)=}
        {len(self.PCapacity)=}"""


def readProblemInstance(nInstance : int):
    filename = f'va_instances/VA{nInstance:02d}.dat'
    file = open(filename, 'r')

    nPeople = int(file.readline()) #first line is n
    cIndividual = list(map(int, file.readline().split())) #second line is c vector

    cPair = [None] * nPeople
    for i in range(nPeople - 1):  # n - 1 lines of matrix c
        cPairLine = [None] * nPeople
        lineRead = list(map(int, file.readline().split()))
        for j in range(len(lineRead)):
            cPairLine[j] = lineRead[j]
        cPair[i] = cPairLine
    print(cPair)

    for i in range(3):      # 3 lines of nothing
        file.readline()

    pWeights = list(map(int, file.readline().split())) # last line is the weights

    if (nPeople - 1)%3 == 0:
        kPlanes = 3
    elif (nPeople - 1)%3 == 1:
        kPlanes = 5
    elif (nPeople - 1)%3 == 2:
        kPlanes = 10

    return problemInstance(nPeople, kPlanes, cIndividual, cPair, pWeights) 

def main():

    print(readProblemInstance(1))

if __name__ == "__main__":
    main()
        

