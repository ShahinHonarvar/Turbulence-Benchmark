
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_truncatable_prime(num):
        digits = list(str(num))
        for i in range(len(digits)):
            if digits[i] == '0':
                return False
            truncated_num = int(''.join(digits[i:]))
            if not is_prime(truncated_num):
                return False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == '0':
                return False
            truncated_num = int(''.join(digits[:i+1]))
            if not is_prime(truncated_num):
                return False
        return True
    
    x = numbers[14]
    primes = []
    for num in range(2, x+1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)
    return primes
