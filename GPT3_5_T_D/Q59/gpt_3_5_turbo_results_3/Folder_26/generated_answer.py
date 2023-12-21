 
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
    result = []
    for n in range(10, x):
        if '0' in str(n):
            continue
        truncated = str(n)
        is_truncatable = True
        while len(truncated) > 1:
            truncated = truncated[1:]
            if not is_prime(int(truncated)):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(n)
    result = sorted(primes, reverse=True)
    return result
