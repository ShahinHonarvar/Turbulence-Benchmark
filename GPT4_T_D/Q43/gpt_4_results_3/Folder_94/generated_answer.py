
def find_primes_between_indices(int_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_nums = [num for num in int_list[10:13] if is_prime(num)]
    return sorted(prime_nums)
