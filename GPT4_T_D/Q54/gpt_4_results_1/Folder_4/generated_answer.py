
def all_right_truncatable_prime(t):
    x = t[96]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        for i in range(len(str(n))):
            if is_prime(n):
                n = n // 10
            else:
                return False
        return True

    lst = [i for i in range(x) if is_right_truncatable(i)]
    lst.sort(reverse=True)
    return lst
