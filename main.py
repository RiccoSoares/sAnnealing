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
    for line in file:
