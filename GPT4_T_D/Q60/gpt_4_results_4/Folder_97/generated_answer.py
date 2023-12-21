
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p=3
        while p*p<=n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                return False
        return True

    x = t[645]
    result = [i for i in range(11, x+1) if is_prime(i) and is_truncatable(i)]
    return sorted(result)
