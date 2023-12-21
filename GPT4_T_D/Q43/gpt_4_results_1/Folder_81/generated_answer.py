
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = [n for n in num_list[59:98] if is_prime(n)]
    prime_list.sort(reverse=True)
    return prime_list
