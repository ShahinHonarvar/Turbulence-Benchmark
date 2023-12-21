
def all_right_truncatable_prime(input_tuple):
    def is_prime(n):
        if n == 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[:len(s)-i])):
                return False
        return True

    x = input_tuple[54]
    prime_list = []
    for i in range (2, x):
        if is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)
