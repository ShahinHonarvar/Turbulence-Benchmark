
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[70]
    primes = []
    for num in range(2, x+1):
        if is_prime(num):
            num_str = str(num)
            if '0' in num_str:
                continue
            for i in range(1, len(num_str)):
                left_truncated = int(num_str[i:])
                right_truncated = int(num_str[:-i])
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    break
            else:
                primes.append(num)
    return primes
