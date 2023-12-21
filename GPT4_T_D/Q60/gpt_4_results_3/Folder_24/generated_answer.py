
def all_left_right_truncatable_prime(tup):
    x = tup[65]
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_LR_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                return False
        return True
    
    results = [n for n in range(10, x+1) if is_prime(n) and is_LR_truncatable(n)]
    return sorted(results, reverse=True)
