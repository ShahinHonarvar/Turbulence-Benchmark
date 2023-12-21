
def all_right_truncatable_prime(lst):
    def is_right_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[:i+1])):
                return False
        return True

    def is_prime(p):
        if p == 1:
            return False
        elif p == 2:
            return True
        else:
            for i in range(2,p):
                if p % i == 0:
                    return False
            return True
            
    x = lst[36]
    truncatable_primes = [i for i in range(2,x) if is_right_truncatable(i)]
    return sorted(truncatable_primes)
