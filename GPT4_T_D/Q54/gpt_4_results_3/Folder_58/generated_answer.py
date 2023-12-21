
def all_right_truncatable_prime(tup):
    x = tup[975]
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True

    return sorted([i for i in range(1, x) if is_right_truncatable_prime(i)],reverse=True)
