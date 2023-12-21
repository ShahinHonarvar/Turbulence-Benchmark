
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated = str(num)
        while truncated:
            if not is_prime(int(truncated)):
                break
            truncated = truncated[1:]
        else:
            primes.append(num)
    return sorted(primes, reverse=True)
