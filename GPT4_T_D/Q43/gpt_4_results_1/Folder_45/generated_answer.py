
def find_primes_between_indices(int_list):
    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    primes = [num for idx, num in enumerate(int_list[23:40]) if check_prime(num)]
    return sorted(primes)
