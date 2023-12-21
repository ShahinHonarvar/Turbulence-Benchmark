
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    start = 69
    end = 84

    primes = []
    for i in range(start, end + 1):
        if is_prime(lst[i]):
            primes.append(lst[i])
    
    return sorted(primes, reverse=True)
