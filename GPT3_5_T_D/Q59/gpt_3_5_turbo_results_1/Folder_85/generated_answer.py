
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[94]
    truncatable_primes = []
    
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_truncatable_prime = True
        truncated_num = num

        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
            truncated_num = int(str(truncated_num)[1:])
        
        if is_truncatable_prime:
            truncatable_primes.append(num)
    
    return truncatable_primes
