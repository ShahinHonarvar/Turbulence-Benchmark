
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_list = [num for num in lst[14:74] if is_prime(num)]
    prime_list.sort(reverse=True)
    return prime_list
