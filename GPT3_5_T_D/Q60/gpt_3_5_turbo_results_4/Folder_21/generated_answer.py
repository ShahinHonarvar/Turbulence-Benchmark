
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            num_str = str(i)
            truncatable_prime = True
            for _ in range(len(num_str) - 1):
                num_str = num_str[1:-1]
                if not is_prime(int(num_str)):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                primes.append(i)
    return sorted(primes)
