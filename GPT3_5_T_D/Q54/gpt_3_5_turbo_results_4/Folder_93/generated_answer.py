
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[11]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            str_num = str(num)
            while len(str_num) > 1:
                str_num = str_num[:-1]
                if not is_prime(int(str_num)):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
