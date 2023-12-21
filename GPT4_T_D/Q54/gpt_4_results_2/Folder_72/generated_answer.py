
def all_right_truncatable_prime(tuple_of_positives):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable(x):
        while x > 0:
            if not is_prime(x):
                return False
            x //= 10
        return True

    x = tuple_of_positives[31]
    return sorted([i for i in range(2, x) if is_right_truncatable(i)], reverse=True)
