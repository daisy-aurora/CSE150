__author__=' daurora@ucsd.edu, A99407185, msarwo@ucsd.edu, A12496484'
import sys

allPrime = []
visited = []

class Node:
	def __init__(self, parent, val, depth):
		self.parent = parent
		self.val = val
		self.depth = depth
		self.lastDepth = self.depth + 1

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

def dfs (startingPrime, finalPrime, depth):
	root = Node(None, startingPrime, 0)
	s = Stack()
	s.append(root)
	curDepth = 0

	path = []
	
	for i in allPrime:
		if(i == startingPrime):
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
				tempPrime = Node(cur, i, curDepth)
				count = 0
				temp1 = int(cur.val)
				temp2 = int(tempPrime.val)
				while temp1 != 0 and temp2 != 0:
					if temp1 % 10 != temp2 % 10:
						count += 1
					temp1 = temp1/10
					temp2 = temp2/10
				if temp1 != 0 or temp2 != 0:
					count = -1
				if(count == 1):
					if(curDepth >= tempPrime.lastDepth + 1):
						continue
					tempPrime.parent = cur
					tempPrime.depth = curDepth + 1
					tempPrime.lastDepth = tempPrime.depth
					s.append(tempPrime)
	return -1

def getPath(startingPrime, finalPrime):
	for i in range(0,9):
		primeList = []
		for j in allPrime:
			prime = Node(None, startingPrime, int(j))
			prime.lastDepth = i + 1
			primeList.append(prime)
		ret = dfs(startingPrime, finalPrime, i)
		if(ret != -1):
			result = ""
			for x in ret:
				result+= str(x) + " "
			return(result)
	return("UNSOLVABLE")


def main():
	primes=str(sys.stdin.readline()).split()
	getAllPrimes(primes[0] ,primes[1])
	
	# THIS PART IS FOR TESTING PURPOSE
# 	for p in allPrime:
# 		print(p),
# 		lists = getPossibleActions(p)
# 		for x in lists:
# 			print(x),
# 		print
	# END OF TESTING CODE
	
	print(getPath(primes[0] ,primes[1]))

if __name__ == '__main__':
	main()
