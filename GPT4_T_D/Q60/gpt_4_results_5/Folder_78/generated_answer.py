
def all_left_right_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
      
    def left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not (is_prime(int(str_n[i:]))) or not (is_prime(int(str_n[:len(str_n) - i]))):
                return False
        return True
    
    for i in range(10, x + 1):
        if left_right_truncatable(i):
            primes.append(i)
   
    return sorted(primes)
