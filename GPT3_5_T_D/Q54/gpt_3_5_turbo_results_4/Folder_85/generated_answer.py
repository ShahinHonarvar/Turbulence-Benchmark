
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[94]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
