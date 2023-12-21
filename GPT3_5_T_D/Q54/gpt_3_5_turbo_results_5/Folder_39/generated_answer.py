
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = []
    for num in range(23, x):
        if is_prime(num):
            truncatable = True
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    primes.sort(reverse=True)
    return primes
