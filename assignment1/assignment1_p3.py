__author__=' daurora@ucsd.edu, A99407185, msarwo@ucsd.edu, A12496484'
import sys

class Node:
	def __init__(self, val):
		self.parent  = None
		self.val = val
        self.depth = 0
		self.lastDepth = depth + 1

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

def getAllPrimes(startingPrime, finalPrime):
    for x in range(int(startingPrime), int(finalPrime)):
        checkPrimeResult = checkPrime(x)
        if checkPrimeResult == True:
            allPrime.append(primeNode)
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

def dfs (startingPrime, finalPrime, depth):
	root = Node(startingPrime, None)
	s = Stack()
	s.append(root)
	curDepth = 0
	path  = []

	for i in allPrime:
		if(i.val == startingPrime):
			allPrime.remove(i)
			break

	while not s.empty():
		cur = s.pop()
		curDepth = cur.depth

		if(cur.val == finalPrime):
			while(cur.parent != None):
				path.insert(0, cur.val)
				cur = cur.parent
			path.insert(0, cur.val)
			return path

		if(curDepth <= depth):
			for i in allPrime:
				count = 0
				temp1 = cur.val
				temp2 = i.val
				while temp1 != 0 and temp2 != 0:
					if temp1 % 10 != temp2 % 10:
						count += 1
					temp1 = temp1/10
					temp2 = temp2/10
				if temp1 != 0 or temp2 != 0:
					counter = -1
				if(counter == 1):
					if(curDepth >= i.lastDepth + 1):
						continue
					i.parent = cur
					i.depth = curDepth + 1
					i.lastDepth = i.depth
					s.append(i)
	return -1

def getPath(startingPrime, finalPrime):
	for i in range(0,9):
		primelist = []
		for j in allPrime:
			j.lastDepth = i + 1
			primeList.append(j)
		ret = dfs(startingPrime, finalPrime, i)
		if(ret != -1):
			print ret
			return ret
	print("UNSOLVABLE")


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

    print(getPath(primes[0] ,primes[1]))

if __name__ == '__main__':
    main()
