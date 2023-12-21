
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    left_truncatable_primes = []
    for num in range(x-1, 1, -1):
        prime = True
        if '0' in str(num):
            continue
        truncated = str(num)
        while truncated:
            if not is_prime(int(truncated)):
                prime = False
                break
            truncated = truncated[1:]
        if prime:
            left_truncatable_primes.append(num)
    return left_truncatable_primes
