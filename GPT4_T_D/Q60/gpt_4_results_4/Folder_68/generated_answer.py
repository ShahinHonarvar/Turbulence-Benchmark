
def all_left_right_truncatable_prime(tup):
    x = tup[1]
    def is_prime(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            left = int(str_n[i:])
            right = int(str_n[:length-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    truncatable_primes = []
    for i in range(x, 10, -1):    # start from x, down to 10
        if is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
