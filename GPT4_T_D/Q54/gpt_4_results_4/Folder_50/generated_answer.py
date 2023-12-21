
def all_right_truncatable_prime(t):
    x = t[57]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        elif is_prime(n):
            return is_truncatable(n // 10)
        else:
            return False

    result = [i for i in range(x) if is_truncatable(i)]
    return sorted(result, reverse=True)
