
def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[71]

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n): 
            return False

        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n)) - i])):
                return False
        return True

    truncatable_primes = []
    for n in range(11, x + 1, 2):
        if is_prime(n) and is_left_right_truncatable(n):
            truncatable_primes.append(n)

    return sorted(truncatable_primes, reverse=True)
