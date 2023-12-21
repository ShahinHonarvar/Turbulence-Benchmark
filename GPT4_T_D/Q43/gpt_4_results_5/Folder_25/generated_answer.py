
def find_primes_between_indices(in_list):
    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in in_list[52:54] if check_prime(i)]
    return sorted(primes)
