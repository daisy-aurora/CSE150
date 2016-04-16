__author__=' daurora@ucsd.edu, A99407185, msarwo@ucsd.edu, A12496484'
import sys
import heapq

allPrime = []
visited = []
path = []

class Node:
    def __init__(self, parent, val, g, h):
        self.parent = parent
        self.val = val
        self.g = g
        self.h = h

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
    def empty(self):
        return self._queue == []

def checkPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    num *= 1.0

    for divisor in range(2, int(num**0.5)+1):
        if num % divisor == 0:
            return False
    return True

def calculateDistance(source, target):
    sourceList = list(map(int, str(source)))
    targetList = list(map(int, str(target)))
    differences = 0
    
    for i in range(0 , len(sourceList)):
        if sourceList[i] != targetList[i]:
            differences += 1
            
    return differences

def getPossibleActions(currentPrime):
    # This method would return the l i s t of prime
    # numbers reachable from current prime .
    # Note - this should not include the prime numbers
    # which have already been processed , either in the
    # frontier or in the closed list .
    listOfPrimes = []

    currPrimeList = list(map(int, str(currentPrime)))

    for prime in allPrime:
        primeList = list(map(int, str(prime)))
        differences = 0
        
        for i in range(0 , len(currPrimeList)):
            if currPrimeList[i] != primeList[i]:
                differences += 1

        if differences == 1:
            isVisited = False
            for visitedNumber in visited:
                if int(visitedNumber) == int(prime):
                    isVisited = True
            if isVisited == False:
                listOfPrimes.append(prime)

    return listOfPrimes

def getAllPrimes(startingPrime, finalPrime):
    startingPrimeLength = len(startingPrime)
    finalPrimeLength = len(finalPrime)
    
    if startingPrimeLength != finalPrimeLength:
        return
    
    for x in range(int(startingPrime), int(finalPrime)):
        checkPrimeResult = checkPrime(x)
        if checkPrimeResult == True:
            allPrime.append(x)
    allPrime.append(finalPrime)

def getPath (startingPrime, finalPrime):
    curDist = 0
    root = Node(None, startingPrime, 0, 0)
    
    pq = PriorityQueue()
    
    pq.push(root, 0)
    
    if startingPrime == finalPrime:
        return str(startingPrime)
    
    while not pq.empty():
        cur = pq.pop()
        curDist = cur.g
        visited.append(cur.val)
        
        if int(cur.val) == int(finalPrime):
            temp = cur
            while temp.parent is not None:
                path.append(temp.val)
                temp = temp.parent
            
            #append the staring prime
            path.append(temp.val)
            
            #reverse the list
            path.reverse()
            
            #convert the list to string
            result = ""
            for x in path:
                result+= str(x) + " "
            return(result)
        
        pList = getPossibleActions(cur.val)
        
        for n in pList:
            #if n not in potential:
            hammingDistance = calculateDistance(finalPrime, n)
            nextNode = Node(cur, n, curDist + 1, hammingDistance)
            estimatedTotalCost = curDist + hammingDistance + 1
            pq.push(nextNode, estimatedTotalCost)
    
    return("UNSOLVABLE")

def main():
    for inputLine in sys.stdin:
        primes=str(inputLine).split()
        getAllPrimes(primes[0] ,primes[1])
        #visited.append(int(primes[0]))
        
        # THIS PART IS FOR TESTING PURPOSE
    #     for p in allPrime:
    #         print(p),
    #         lists = getPossibleActions(p)
    #         for x in lists:
    #             print(x),
    #         print
        # END OF TESTING CODE
    
        sys.stdout.write(getPath(primes[0] ,primes[1]))
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()