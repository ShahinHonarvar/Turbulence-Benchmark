
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
    
    try:
        primes = [i for i in lst[69:85] if is_prime(i)]
        primes.sort(reverse=True)
        return primes
    except IndexError:
        return []
