
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_list = [num for num in num_list[29:98] if is_prime(num)]
    prime_list.sort(reverse=True)
    return prime_list
