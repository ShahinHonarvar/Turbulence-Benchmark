
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_nums = []
    for i in range(33, 36):
        if is_prime(num_list[i]):
            prime_nums.append(num_list[i])
    return sorted(prime_nums)
