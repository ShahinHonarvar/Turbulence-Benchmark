
def find_primes_between_indices(integer_list):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True

    primes = [i for i in integer_list[131:816] if is_prime(i)]
    primes.sort(reverse=True)
    return primes
