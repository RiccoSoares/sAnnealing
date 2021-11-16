import numpy as np
import copy
import random
import planetrips

class Solution:
    def __init__(self, instance : planetrips.Instance):
        self.__instance = instance
        self.vMatrix = np.zeros((self.__instance.kPlanes, self.__instance.nPeople))
        self.freeSpace = self.__calculateFreeSpace()
        self.value = 0

    def __calculateFreeSpace(self):
        freeSpace = np.zeros(self.__instance.kPlanes)
        for plane in range(self.__instance.kPlanes):
            planeWeight = np.sum(self.__instance.pWeights * self.vMatrix[plane])
            freeSpace[plane] = self.__instance.PCapacity[plane] - planeWeight 
        return freeSpace

    def randomNeighbourStep(self):
        nonFeasible = True
        while(nonFeasible):
            plane = random.randint(0, self.__instance.kPlanes - 1)
            person = random.randint(0, self.__instance.nPeople - 1)
            if(self.vMatrix[plane][person]):
                self.deallocate(person, plane)
                nonFeasible = False
            elif(not np.sum(self.vMatrix[:,person])) and self.__instance.pWeights[person] <= self.freeSpace[plane]:
                self.allocate(person, plane)
                nonFeasible = False

    def allocate(self, person, plane):
        self.vMatrix[plane][person] = 1
        personValue = self.__instance.cIndividual[person]
        personValue += np.sum(self.__instance.cPair[person] * self.vMatrix[plane])
        self.value += personValue

    def deallocate(self, person, plane):
        self.vMatrix[plane][person] = 0
        personValue = self.__instance.cIndividual[person]
        personValue += np.sum(self.__instance.cPair[person] * self.vMatrix[plane])
        self.value -= personValue
        
    def getAllocation(self, person, plane):
        return self.vMatrix[plane][person]
        
    def invAllocation(self, person, plane):
        if self.getAllocation(person, plane):
            self.deallocate(person, plane)
        else:
            self.allocate(person, plane)


    def isFeasible(self): #determines wether or not a solution is feasible
        planesPerPerson = self.vMatrix.sum(axis=0) 

        #sum of planes per person is bool, only one or zero
        onePlanePerPerson = np.array_equal(planesPerPerson, planesPerPerson.astype(bool))
        if not onePlanePerPerson:
            return False
        plane = 0
        for row in self.vMatrix:
            planeWeight = 0
            for person in range(self.__instance.nPeople):
                planeWeight += row[person]*self.__instance.pWeights[person]
                if planeWeight > self.__instance.PCapacity[plane]:
                    return False    
            plane += 1

        return True
        
    def evaluate(self): #returns the profit assured by given solution or -1 in case the solution is not feasible.
        if self.isFeasible():
            val = 0
            
            for plane in range(self.__instance.kPlanes):
                for person in range(self.__instance.nPeople):
                    if (self.getAllocation(person, plane)):  #if the person is allocated to the plane
                        val += self.__instance.cIndividual[person]
                        
                    for anotherPerson in range(self.__instance.nPeople):
                        if (self.getAllocation(anotherPerson, plane)):
                            val += self.__instance.cPair[person][anotherPerson]
                    
            return val
        else:
            return -1
        
    def __str__(self):
        return str(self.vMatrix)

    def __copy__(self):
        memo = {id(self.__instance): copy.copy(self.__instance)} 
        return copy.deepcopy(self, memo)
