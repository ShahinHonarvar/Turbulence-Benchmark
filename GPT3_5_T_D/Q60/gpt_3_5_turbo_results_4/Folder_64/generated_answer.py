
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[4]
    truncatable_primes = []
    
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        if is_prime(num):
            num_str = str(num)
            is_truncatable = True
            for i in range(1, len(num_str)):
                left_truncation = int(num_str[i:])
                right_truncation = int(num_str[:i])
                if not is_prime(left_truncation) or not is_prime(right_truncation):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    
    return truncatable_primes
