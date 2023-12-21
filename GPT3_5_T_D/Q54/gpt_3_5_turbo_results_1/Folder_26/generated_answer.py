
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = t[81]
    result = []
    
    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    
    for i in range(x-1, 0, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    
    return sorted(result, reverse=True)
