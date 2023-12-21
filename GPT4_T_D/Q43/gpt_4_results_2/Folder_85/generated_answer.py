
def find_primes_between_indices(integer_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_list = [x for x in integer_list[32:36] if is_prime(x)]
    prime_list.sort()
    return prime_list
