
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(len(lst)):
        if i >= 131 and i <= 815 and is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort(reverse=True)
    return primes
