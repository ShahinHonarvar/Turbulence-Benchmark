
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[803]
    left_truncatable_primes = []
    
    for n in range(2, x):
        if '0' not in str(n):
            truncated_number = str(n)
            while len(truncated_number) > 1:
                truncated_number = truncated_number[1:]
                if not is_prime(int(truncated_number)):
                    break
            else:
                left_truncatable_primes.append(n)
    
    return sorted(left_truncatable_primes)
