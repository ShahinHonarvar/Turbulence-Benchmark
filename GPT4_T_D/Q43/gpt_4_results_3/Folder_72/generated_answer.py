
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    lst = lst[28:45]
    primes = [num for num in lst if is_prime(num)]
    primes.sort()
    return primes
