
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for i in range(2, numbers[54] + 1):
        if '0' not in str(i) and is_prime(i):
            num_str = str(i)
            while len(num_str) > 1 and is_prime(int(num_str[1:])) and is_prime(int(num_str[:-1])):
                num_str = num_str[1:-1]
            if len(num_str) <= 2:
                primes.append(i)
    return sorted(primes, reverse=True)
