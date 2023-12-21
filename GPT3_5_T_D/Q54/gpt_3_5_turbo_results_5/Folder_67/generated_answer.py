
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[71]
    right_truncatable_primes = []
    
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            is_right_truncatable = True
            temp_num = num // 10
            
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_right_truncatable = False
                    break
                temp_num = temp_num // 10
            
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes, reverse=True)
