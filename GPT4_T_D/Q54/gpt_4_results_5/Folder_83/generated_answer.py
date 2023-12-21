
def all_right_truncatable_prime(t):
    x = t[24]
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    result = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
