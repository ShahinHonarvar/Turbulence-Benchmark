
def find_primes_between_indices(lst):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [i for i in lst[43:60] if is_prime(i)]
    primes.sort(reverse=True)
    
    return primes
