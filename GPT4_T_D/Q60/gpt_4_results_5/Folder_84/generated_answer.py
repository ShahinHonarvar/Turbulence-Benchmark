
def all_left_right_truncatable_prime(integers):
    x = integers[630]
    primes = []

    def is_prime(n):
        if n<2:
            return False
        elif n==2 or n==3:
            return True
        elif n%2==0 or n%3==0:
            return False
        
        for i in range(5, int(n**0.5) + 1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all([is_prime(int(str(n)[i:]+str(n)[:i])) for i in range(len(str(n)))])

    for i in range(11, x+1):
        if is_truncatable_prime(i):
            primes.append(i)
            
    return sorted(primes, reverse=True)
