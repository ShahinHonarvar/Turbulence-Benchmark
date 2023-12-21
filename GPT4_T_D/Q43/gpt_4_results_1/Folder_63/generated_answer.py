
def find_primes_between_indices(int_list):
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

    if len(int_list) < 36:
        return []

    ints_to_check = int_list[28:37]
    primes = sorted([num for num in ints_to_check if is_prime(num)])
    return primes
