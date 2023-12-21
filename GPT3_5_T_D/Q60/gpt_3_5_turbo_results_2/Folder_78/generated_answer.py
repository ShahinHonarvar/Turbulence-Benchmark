
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[23]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            if '0' in num_str:
                continue
            left_truncated = True
            right_truncated = True
            while left_truncated and len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    left_truncated = False
            while right_truncated and len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    right_truncated = False
            if left_truncated and right_truncated:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
