
def all_left_right_truncatable_prime(tup):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable(n):
        str_num = str(n)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num)-i])):
                return False
        return True
    
    x = tup[784]
    truncatable_primes = []
    for i in range(10, x+1):
        if is_prime(i) and is_truncatable(i):
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes
