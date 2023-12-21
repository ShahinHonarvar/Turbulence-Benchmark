
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(n):
        string_num = str(n)
        for i in range(1, len(string_num)):
            if not is_prime(int(string_num[i:])):
                return False
        return True
    
    x = numbers[87]
    left_truncatable_primes = []
    
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes)
