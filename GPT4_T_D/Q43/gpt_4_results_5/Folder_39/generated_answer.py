
def find_primes_between_indices(lst):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(69, 81):
        if i < len(lst) and is_prime(lst[i]):
            primes.append(lst[i])

    return sorted(primes)
