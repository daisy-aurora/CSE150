__author__ = ’ daurora@ucsd.edu , A99407185 , student2@ucsd.edu , student2PID ’

def checkPrime(input):
	if input < 2:
		return False
	if input == 2:
		return True
	input *= 1.0

	for divisor in range (2, int(input**0.5)+1):
		if input % divisor == 0:
			return False
	return True

def getPossibleActions(currentPrime):
	# This method would return the l i s t of prime
	# numbers reachable from current prime .
	# Note − this should not include the prime numbers
	# which have already been processed , either in the
	# frontier or in the closed list .
	return listOfPrimes

def getPath(startingPrime ,finalPrime): 
	# your code here
	return path

def main():
	primes=str(sys.stdin.readline()).split() 
	print(getPath(primes[0] ,primes[1]))

if __name__ == ’__main__’: 
	main()