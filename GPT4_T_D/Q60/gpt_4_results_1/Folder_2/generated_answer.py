
def all_left_right_truncatable_prime(tup):
    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:length-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    truncatable_primes = []
    x = tup[618]
    for n in range(x):
        if is_left_right_truncatable_prime(n):
            truncatable_primes.append(n)
    return truncatable_primes
