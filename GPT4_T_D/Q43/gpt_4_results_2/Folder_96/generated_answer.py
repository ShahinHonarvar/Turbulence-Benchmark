
def find_primes_between_indices(input_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    primes = [num for num in input_list[31:68] if is_prime(num)]
    return sorted(primes, reverse=True)
