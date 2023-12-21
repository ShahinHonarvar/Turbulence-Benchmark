
def all_left_right_truncatable_prime(tup):
    def is_prime(n):
        if n<=1:
            return False
        if n == 2 or n == 3:
            return True
        if n%2 == 0 or n%3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n%i == 0 or n%(i+2) == 0:
                return False
            i += 6
        return True
        
    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
            if not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    x = tup[10]
    return sorted([i for i in range(x+1) if is_prime(i) and is_truncatable(i)], reverse=True)
