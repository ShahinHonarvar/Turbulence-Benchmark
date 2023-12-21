
def find_primes_between_indices(input_list):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    primes = [num for num in input_list[55:77] if is_prime(num)]
    primes.sort()
    return primes
