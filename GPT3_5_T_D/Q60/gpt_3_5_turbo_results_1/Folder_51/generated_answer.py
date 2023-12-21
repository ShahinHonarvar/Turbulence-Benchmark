
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if '0' in str(num):
            continue
        num_str = str(num)
        is_left_right_truncatable = True
        for i in range(len(num_str), 1, -1):
            if not is_prime(int(num_str[:i])):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            primes.append(num)
    return sorted(primes)
