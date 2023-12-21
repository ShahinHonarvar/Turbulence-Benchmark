
import math

def all_left_right_truncatable_prime(n):
    # find primes less than or equal to n
    primes = []
    for prime in range(2, int(math.ceil(math.log(n, 2)) + 1)):
        # check if prime is left-and-right-truncatable
        if str(prime).count("0") == 0:
            # remove leading and trailing digits
            while str(prime).count("0") == 0:
                prime = int(str(prime)[1:])
            while str(prime).count("0") == 0:
                prime = int(str(prime)[-1:])
            # add prime to list
            primes.append(prime)
    # return list of all left-and-right-truncatable primes
    return sorted(primes) if primes else []
