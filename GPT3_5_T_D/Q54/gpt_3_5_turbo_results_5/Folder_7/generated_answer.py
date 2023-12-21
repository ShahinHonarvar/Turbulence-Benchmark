
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[803]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            is_truncatable = True
            for i in range(1, len(num_str)):
                trunc_num = int(num_str[:-i])
                if not is_prime(trunc_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
