
def all_left_truncatable_prime(tup):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num = str(n)
        if '0' in num:
            return False
        for i in range(len(num)):
            if not is_prime(int(num[i:])):
                return False
        return True

    x = tup[803]
    prime_list = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)
