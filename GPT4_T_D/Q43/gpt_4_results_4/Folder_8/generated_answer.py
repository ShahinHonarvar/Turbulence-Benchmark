
def find_primes_between_indices(lst):
    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_list = [i for i in lst[43:77] if check_prime(i)]
    return sorted(prime_list, reverse=True)
