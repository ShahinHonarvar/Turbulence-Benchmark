
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(arr):
    index = 478
    factors = set()
    num = arr[index]
    for i in range(2, num + 1):
         if num % i == 0:
            if is_prime(i):
                factors.add(i)
    return factors
