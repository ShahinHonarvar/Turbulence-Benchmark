
def all_right_truncatable_prime(tup):
    x = tup[4]
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_trunc(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    
    return sorted([i for i in range(x) if right_trunc(i)])
