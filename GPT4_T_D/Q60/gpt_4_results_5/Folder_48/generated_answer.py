
def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    
    def is_prime(n):
        if n <= 1: return False
        if n == 2 or n == 3: return True
        if n % 2 == 0: return False
        i = 3
        while i * i <= n:
            if n % i == 0: return False
            i += 2
        return True

    def is_left_and_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n: return False
        
        for i in range(1, len(str_n)):   
            if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i]))):
                return False
        return True

    for n in range(2, x + 1):
        if is_prime(n) and is_left_and_right_truncatable(n):
            primes.append(n)
    
    return primes
