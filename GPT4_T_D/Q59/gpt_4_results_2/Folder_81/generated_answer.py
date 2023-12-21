
def all_left_truncatable_prime(t):
    x = t[98]
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
        
    def left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    res = [i for i in range(10, x) if left_truncatable(i)]
    res.sort()
    return res
