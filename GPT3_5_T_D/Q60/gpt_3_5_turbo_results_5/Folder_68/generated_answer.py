
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in range(numbers[1], 0, -1):
        if '0' not in str(x) and is_prime(x):
            x_str = str(x)
            while len(x_str) > 2:
                x_str = x_str[1:-1]
                if not is_prime(int(x_str)):
                    break
            else:
                primes.append(x)
    return primes
