
def find_primes_between_indices(lst):
    # Checking for prime numbers
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    # Filtering out primes between indices 149 and 979
    prime_lst = []
    for i in range(149, 980):
        if i < len(lst) and is_prime(lst[i]):
            prime_lst.append(lst[i])
    return sorted(prime_lst)
