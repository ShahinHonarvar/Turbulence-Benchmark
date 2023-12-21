
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return sorted([x for x in lst[19:72] if is_prime(x)])
