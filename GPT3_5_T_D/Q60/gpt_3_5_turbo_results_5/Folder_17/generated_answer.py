
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    x = numbers[36]
    for num in range(x, 9, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable_prime = True
        # Check left truncatable prime
        for i in range(len(str_num)-1, 0, -1):
            left_truncated = int(str_num[:i])
            if not is_prime(left_truncated):
                is_truncatable_prime = False
                break
        if not is_truncatable_prime:
            continue
        # Check right truncatable prime
        for i in range(1, len(str_num)):
            right_truncated = int(str_num[i:])
            if not is_prime(right_truncated):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
