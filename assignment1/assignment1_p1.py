__author__=' daurora@ucsd.edu, A99407185, '
import sys

allPrime = []

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
            listOfPrimes.append(prime)
    
    return listOfPrimes

def getPath(startingPrime ,finalPrime): 
    # your code here
    path = 0
    return path

def getAllPrimes(startingPrime, finalPrime):
    for x in range(int(startingPrime), int(finalPrime)):
        checkPrimeResult = checkPrime(x)
        if checkPrimeResult == True:
            allPrime.append(x)
    allPrime.append(finalPrime)

def main():
    primes=str(sys.stdin.readline()).split()
    getAllPrimes(primes[0] ,primes[1])
    
    # THIS PART IS FOR TESTING PURPOSE
    for p in allPrime:
        print(p),
        lists = getPossibleActions(p)
        for x in lists:
            print(x),
        print
    # END OF TESTING CODE
    
    #print(getPath(primes[0] ,primes[1]))

if __name__ == '__main__':
    main()