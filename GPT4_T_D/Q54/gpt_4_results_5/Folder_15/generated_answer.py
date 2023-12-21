
def all_right_truncatable_prime(t):
    from sympy import isprime

    def check(num):
        num = str(num)
        for i in range(len(num)):
            if not isprime(int(num[0:i+1])):
                return False
        return True
    
    x = t[6]
    return sorted([i for i in range(2, x) if check(i)], reverse=True)
