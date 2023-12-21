
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    primes = [num for num in int_list[45:81] if is_prime(num)]
    primes.sort(reverse=True)

    return primes
