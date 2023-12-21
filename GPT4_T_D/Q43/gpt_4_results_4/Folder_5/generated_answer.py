
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    sub_list = int_list[27:87]
    primes = [i for i in sub_list if is_prime(i)]
    primes.sort(reverse = True)
    return primes
