
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = []
    for i in range(157, 736):
        if is_prime(lst[i]):
            primes.append(lst[i])
    
    return sorted(primes, reverse=True)
