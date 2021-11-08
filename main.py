class airplaneTrips:
    def __init__(self, nPeople, kPlanes, cIndividual, cPair, pWeights):
        self.nPeople = nPeople
        self.kPlanes = kPlanes
        self.cIndividual = cIndividual
        self.cPair = cPair
        self.pWeights = pWeights
        self.PCapacity = calculatePlaneCapacity(pWeights, kPlanes)

    def calculatePlaneCapacity(pWeights, kPlanes):
        planeCapacity = [None] * kPlanes
        totalWeight = sum(pWeights)
        for k in range(kPlanes):
            planeCapacity[k] = 0.8 * (totalWeight/k)
        return planeCapacity


def createProblemInstance(filename):
    file = open(filename, 'r')
    nPeople = int(file.readline())
    cIndividual = list(map(int, file.readline().split()))
    cPair = []
    for i in range(nPeople):
        cPair.append(list(map(int, file.readline().split())))
    for i in range(3):
        file.readline()
    pWeights = file.readline()
    newInstance = airplaneTrips(nPeople, kPlanes, cIndividual, cPair, pWeights)
    return newInstance
