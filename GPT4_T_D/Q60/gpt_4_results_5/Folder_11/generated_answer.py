
def all_left_right_truncatable_prime(num_tuple):
    
    # To check if a number is prime
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    # To check if a number is truncatable from left and right
    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = num_tuple[86]
    primes = [n for n in range(2, x+1) if is_prime(n) and '0' not in str(n) and is_truncatable(n)]
    return sorted(primes)
