
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if len(num_list) < 72:
        return []
    else:
        primes = [i for i in num_list[70:72] if is_prime(i)]
        primes.sort(reverse=True)
        return primes
