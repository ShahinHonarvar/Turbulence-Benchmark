
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 11:
            continue
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                break
        else:
            x_str = str(x)
            if '0' in x_str:
                continue
            for i in range(1, len(x_str)):
                left = int(x_str[i:])
                right = int(x_str[:-i])
                if not is_prime(left) or not is_prime(right):
                    break
            else:
                primes.append(x)
    primes.sort(reverse=True)
    return primes
