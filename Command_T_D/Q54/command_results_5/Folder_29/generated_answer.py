import sys
def all_right_truncatable_prime(nums):
    # your code here
    primes = []
    # find all prime numbers less than 55
    # use n=nums[55] to find the prime numbers less than 55
    for n in range(2, int(str(nums[55])[0])+1):
        # check if n is prime
        if all(n%d!=0 for d in range(2, int(str(n))[0]+1)):
            # check if n is right truncatable
            if n%2!=0 and str(n)[-1]!='5' and str(n)[-1]!='0':
                # if it is, add it to the list of primes
                primes.append(n)
    return primes
