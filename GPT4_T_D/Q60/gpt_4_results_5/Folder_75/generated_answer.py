
def all_left_right_truncatable_prime(tup):
    x = tup[41]
    
    def isPrime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def leftandright_truncatable(n):
        str_n = str(n)
        if '0' in str_n: return False
        return all(isPrime(int(str_n[i:])) and isPrime(int(str_n[:i+1])) for i in range(len(str_n)))

    return sorted([i for i in range(11, x+1) if isPrime(i) and leftandright_truncatable(i)])
