def find_primes_between_indices(lst):
    return sorted(filter(prime, lst[55:76]))
def prime(x):
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    else:
        maxDivisor = x**0.5
        d, i = 5, 2
        while d <= maxDivisor:
            if x % d == 0:
                return False
            d += i
            i = 6 - i
