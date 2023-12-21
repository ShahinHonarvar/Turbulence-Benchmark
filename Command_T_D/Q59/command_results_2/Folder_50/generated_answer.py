def all_left_truncatable_prime(x):
    # primes
    p = list(range(2, x)) + [x]
    # is_prime
    def is_prime(n):
        # is_natural
        if n < 1:
            return False
        # is_even
        if n % 2 == 0:
            return False
        # is_divisor
        for i in range(3, int(n ** .5) + 1):
            if n % i == 0:
                return False
        return True
    # remove_left_ Digits
    def remove_left_digits(n):
        l = str(n)
        for i in range(1, len(l)):
            if l[i - 1] != '9':
                l = l[i:]
                break
        if l:
            return int(''.join(l))
    # right_truncatable_prime
    def right_truncatable_prime(n):
        # is_prime
        if is_prime(n):
            # remove_left_digits
            for d in range(2, n // 2 + 1):
                if remove_left_digits(n - d) == n:
                    return True
            return False
    # left_truncatable_prime
    def left_truncatable_prime(n):
        # is_prime
        if is_prime(n):
            # remove_left_digits
            for d in range(2, n // 2 + 1):
                if remove_left_digits(d) == n:
                    return True
            return False
    # all_left_truncatable_prime
    res = []
    for n in p:
        if left_truncatable_prime(n):
            res.append(n)
    return sorted(res)[::-1]
