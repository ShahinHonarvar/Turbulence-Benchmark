
def find_primes_between_indices(int_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_nums = [i for i in int_list[37:96] if is_prime(i)]
    return sorted(prime_nums, reverse=True)
