__author__=' daurora@ucsd.edu, A99407185, msarwo@ucsd.edu, A12496484'
import sys

allPrime = []
visited = []
path = []

class Node:
    def __init__(self, parent, val, depth):
        self.parent = parent
        self.val = val
        self.depth = depth

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

class Stack:
    def append(self, val):
        self.elts.append(val)
    def pop(self):
        return self.elts.pop()
    def size(self):
        return len(self.elts)
    def empty(self):
        return self.elts == []
    def __init__(self):
            self.elts = []

def getPath (startingPrime, finalPrime):
    root = Node(None, startingPrime, 0)
    s = Stack()
    s.append(root)
    curDepth = 0

    #COMMENTED OUT
#     for i in allPrime:
#         if i == startingPrime:
#             allPrime.remove(i)
#             break
    if startingPrime == finalPrime:
        return str(startingPrime)

    while not s.empty():
        cur = s.pop()
        #print("I'm here bro")
            
        curDepth = cur.depth
#         print(cur.val),
#         print(curDepth)
        # COMMENTED OUT, POSSIBLE WRONG CODE?
#         if(cur.val == finalPrime):
#             while(cur.parent != None):
#                 path.insert(0, cur.val)
#                 cur = cur.parent
#             path.insert(0, cur.val)
#             return path
        numberAlreadyVisited = False
        for visitedNumbers in visited:  
            # TEST CODE 
#             print("check :"),
#             print(visitedNumbers),
#             print("vs "),
#             print(cur.val) 
            # END OF TEST CODE
            if int(cur.val) == int(visitedNumbers):
#                 print("same! so it's already been visited!")
                numberAlreadyVisited = True
        
        #number has not been visited, set it as visited
        if numberAlreadyVisited == False:
            # TEST CODE
#             print("not visited! pushed: "),
#             print(cur.val)
            # END OF TEST CODE
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
#         for y in pList:
#             print(y),
#         print
        
        pList.reverse()
        if(curDepth < 5):
            for i in pList:
                #print(i), 
                #COMMENTED OUT
#                 i.depth = curDepth + 1
#                 s.append(i)
                nextNode = Node(cur, i, curDepth + 1)
                # TEST CODE
#                 print("push stack: "),
#                 print("parent: "),
#                 print(cur.val),
#                 print("value: "),
#                 print(i)
                # TEST CODE
                s.append(nextNode)
    
    return("UNSOLVABLE")

def main():
    primes=str(sys.stdin.readline()).split()
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

    print(getPath(primes[0] ,primes[1]))

if __name__ == '__main__':
    main()
