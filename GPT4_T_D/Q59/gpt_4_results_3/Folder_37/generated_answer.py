
def all_left_truncatable_prime(tup):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    x = tup[35]
    return sorted([num for num in range(2, x) if is_left_truncatable_prime(num)], reverse=True)
