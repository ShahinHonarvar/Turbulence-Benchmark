
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    left_truncatable_primes = []
    
    for num in range(2, x):
        if '0' not in str(num):
            truncated_num = str(num)
            while len(truncated_num) > 0:
                if not is_prime(int(truncated_num)):
                    break
                truncated_num = truncated_num[1:]
            else:
                left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes, reverse=True)
