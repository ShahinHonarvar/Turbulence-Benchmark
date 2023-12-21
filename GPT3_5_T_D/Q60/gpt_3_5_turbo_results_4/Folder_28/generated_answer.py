
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
        if num < 10:
            continue
        string_num = str(num)
        if '0' in string_num:
            continue
        is_truncatable_prime = True
        for i in range(1, len(string_num)):
            left_truncated = int(string_num[i:])
            right_truncated = int(string_num[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            primes.append(num)
    primes.sort()
    return primes
