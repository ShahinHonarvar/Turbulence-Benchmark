
def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
            
    def is_right_truncatable(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i+1])) for i in range(len(str_n)))
        
    x = tup[429]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
            
    return sorted(primes, reverse=True)
