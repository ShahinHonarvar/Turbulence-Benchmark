
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[28]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        is_left_truncatable = True
        for j in range(len(str(i))):
            truncated_number = str(i)[j:]
            if not is_prime(int(truncated_number)):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
