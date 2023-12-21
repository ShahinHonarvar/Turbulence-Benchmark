
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
        for i in range(2, x):
            if is_prime(i):
                i_str = str(i)
                if '0' not in i_str:
                    truncatable = True
                    for j in range(1, len(i_str)):
                        if not is_prime(int(i_str[:-j])) or not is_prime(int(i_str[j:])):
                            truncatable = False
                            break
                    if truncatable:
                        primes.append(i)
    return sorted(primes)
