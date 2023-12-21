
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 2:
            continue
        x_str = str(x)
        if '0' in x_str:
            continue
        is_left_right_truncatable_prime = True
        # Check left truncation
        for i in range(1, len(x_str)):
            left_truncated_num = int(x_str[i:])
            if not is_prime(left_truncated_num):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            # Check right truncation
            for i in range(len(x_str) - 1, 0, -1):
                right_truncated_num = int(x_str[:i])
                if not is_prime(right_truncated_num):
                    is_left_right_truncatable_prime = False
                    break
        if is_left_right_truncatable_prime:
            primes.append(x)
    return sorted(primes)
