__author__=' daurora@ucsd.edu, A99407185, msarwo@ucsd.edu, A12496484'
import sys
import Queue

allPrime = []
visited = []
path = []

out = sys.stdout

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
        return str(startingPrime)
    
    while not q.empty():
        # CODE TEST HERE
#         for elem in list(q.queue):
#             print(elem.val), 
#             print("parent: "),
#             if elem.parent == None:
#                 print("None"),
#             else:
#                 print(elem.parent.val),
#             print(","),
#         print
        # END OF CODE TEST
        cur = q.get()
        #potential.add(cur.val)
        if cur.val == finalPrime:
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
    for inputLine in sys.stdin:
        primes=str(inputLine).split()
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
        
        resultText = getPath(primes[0] ,primes[1])
        
        out.write(resultText)
        out.write('\n')
    #    out.close()

if __name__ == '__main__':
    main()
