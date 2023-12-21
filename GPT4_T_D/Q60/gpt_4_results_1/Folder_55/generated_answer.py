
def all_left_right_truncatable_prime(t):
    from sympy import isprime
    def check_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    def check_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not check_prime(int(str_n[i:])) or not check_prime(int(str_n[:len(str_n)-i])):
                return False
        return True
    x = t[73]
    result = []
    for i in range(11, x + 1):
        if check_prime(i) and check_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
