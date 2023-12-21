
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_nums = [i for i in num_list[187:272] if is_prime(i)]
    return sorted(prime_nums)
