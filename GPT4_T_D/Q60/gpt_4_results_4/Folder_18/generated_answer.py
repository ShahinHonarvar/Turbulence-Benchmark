
def all_left_right_truncatable_prime(args):
    def is_prime(n):
        if n <= 1 or (n%2 == 0 and n>2): 
            return False
        return all(n%i for i in range(3, int(n**0.5) + 1, 2))
    
    def is_left_right_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:-i])):
                return False
        return True
    
    x = args[429]
    truncatable_primes = [i for i in range(10, x+1) if is_prime(i) and is_left_right_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)
