
def find_primes_between_indices(lst):
    
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = round(n**0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    primes = []

    for i in range(19, 72):
        if is_prime(lst[i]):
            primes.append(lst[i])

    return sorted(primes)
