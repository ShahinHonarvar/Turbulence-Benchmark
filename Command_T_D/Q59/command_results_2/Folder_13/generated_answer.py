import sys
def all_left_truncatable_prime(n):
    primes = []
    for i in range(3, n[0]+1):
        if all(str(i).rstrip('0').rstrip('') == str(j) for j in range(2, int(str(i))+1)):
            primes.append(i)
    return sorted(primes)
