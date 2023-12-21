
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:len(str(n)) - i])):
                return False
        return True

    x = tup[630]
    result = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(result, reverse=True)
