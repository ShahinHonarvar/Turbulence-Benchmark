
def all_left_right_truncatable_prime(tple):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def is_truncatable(n):
        str_num = str(n)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num)-i])):
                return False
        return True
    
    x = tple[71]
    truncatable_primes = []
    for num in range(10, x+1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
            
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
