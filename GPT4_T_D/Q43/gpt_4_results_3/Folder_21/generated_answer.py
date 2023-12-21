
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [num for num in num_list[478:950] if is_prime(num)]
    return sorted(primes, reverse=True)
