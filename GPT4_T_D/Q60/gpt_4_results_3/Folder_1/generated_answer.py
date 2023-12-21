
def all_left_right_truncatable_prime(tup):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num_length = len(str(n))
        for i in range(num_length):
            left_trunc = int(str(n)[i:])
            right_trunc = int(str(n)[:num_length-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True

    x = tup[20]
    truncatable_primes = [i for i in range(11, x+1) if is_left_right_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
