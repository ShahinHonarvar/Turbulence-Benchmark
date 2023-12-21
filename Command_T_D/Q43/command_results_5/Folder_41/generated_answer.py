def find_primes_between_indices(lst):
    return sorted(list(filter(prime, lst[45:80])), reverse=True)
def prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        maxDivisor = int(n ** .5)
        for i in range(5, maxDivisor + 1):
            if n % i == 0:
                return False
        return True
