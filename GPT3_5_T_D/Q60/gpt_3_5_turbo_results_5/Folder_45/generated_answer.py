
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        truncatable_prime = True
        num_str = str(num)
        while len(num_str) > 1:
            if not is_prime(int(num_str)):
                truncatable_prime = False
                break
            num_str = num_str[1:-1]
        if truncatable_prime:
            primes.append(num)
    return sorted(primes)
