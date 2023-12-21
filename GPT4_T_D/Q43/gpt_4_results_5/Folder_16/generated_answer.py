
def find_primes_between_indices(int_list):
    prime_nums = []
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
    for i in range(424, 553):
        if i < len(int_list) and is_prime(int_list[i]):
            prime_nums.append(int_list[i])
    return sorted(prime_nums, reverse=True)
