
def find_primes_between_indices(lst):
    def check_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    lst = lst[69:81]

    return sorted(list(filter(check_prime, lst)))
