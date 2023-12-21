
def find_primes_between_indices(lst):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    filtered_list = lst[187:272]
    prime_list = [x for x in filtered_list if is_prime(x)]
    return sorted(prime_list)
