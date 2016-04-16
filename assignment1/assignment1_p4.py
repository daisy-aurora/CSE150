__author__=' daurora@ucsd.edu, A99407185, msarwo@ucsd.edu, A12496484'
import sys
import Queue

allPrime = []
visited = []
path = []

class Node:
    def __init__(self, parent, val):
        self.parent = parent
        self.val = val

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
                if visitedNumber == prime:
                    isVisited = True
            if isVisited == False:
                listOfPrimes.append(prime)
                visited.append(prime)

    return listOfPrimes

def getPath(startingPrime ,finalPrime):
    # your code here
    root = Node(None, startingPrime)
    q = Queue.Queue()
    q.put(root)

    if startingPrime == finalPrime:
        path.append(root.val)
        print(startingPrime)
        print(finalPrime)
    while not q.empty():
        cur = q.get()
        if cur.val == finalPrime:
            temp = cur
            while temp.parent is not None:
                path.append(temp.val)
                temp = temp.parent

            #append the staring prime
            path.append(temp.val)

            result2 = ""
            for x in path:
                if(x != startingPrime):
                    result2 += str(x) + " "
                    
            #reverse the list
            path.reverse()

            #convert the list to string
            result1 = ""
            for x in path:
                if(x != finalPrime):
                    result1 += str(x) + " "
            
            result = result1 + "\n" + result2
            return(result)
            
        pList = getPossibleActions(cur.val)
        for n in pList:
            #if n not in potential:
            nextNode = Node(cur, n)
            q.put(nextNode)

    return("UNSOLVABLE")

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

def main():
    primes=str(sys.stdin.readline()).split()
    getAllPrimes(primes[0] ,primes[1])
    visited.append(int(primes[0]))

    # THIS PART IS FOR TESTING PURPOSE
    #for p in allPrime:
    #    print(p),
    #    lists = getPossibleActions(p)
    #    for x in lists:
    #        print(x),
    #    print
    # END OF TESTING CODE

    print(getPath(primes[0] ,primes[1]))

if __name__ == '__main__':
    main()
