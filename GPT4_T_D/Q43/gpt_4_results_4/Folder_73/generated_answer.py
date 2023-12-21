
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    primes = [number for index, number in enumerate(lst[19:91]) if is_prime(number)]
    return sorted(primes, reverse=True)
