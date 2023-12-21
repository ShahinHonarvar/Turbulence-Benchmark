
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[49]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            num_str = str(i)
            while len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes
