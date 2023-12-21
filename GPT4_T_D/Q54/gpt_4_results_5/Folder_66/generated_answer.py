
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True     
    
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i+1])) for i in range(len(str_n)))

    x = tup[25]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)
