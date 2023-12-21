
def find_primes_between_indices(int_list):
    primes = []
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True
    for i in range(75, 86):
        if i < len(int_list) and is_prime(int_list[i]):
            primes.append(int_list[i])
    return sorted(primes)
