
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        return False

    primes = [num for num in num_list[32:36] if is_prime(num)]
    return sorted(primes)
