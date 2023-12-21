
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[992]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                truncatable_num = int(num_str[i:])
                if not is_prime(truncatable_num):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
