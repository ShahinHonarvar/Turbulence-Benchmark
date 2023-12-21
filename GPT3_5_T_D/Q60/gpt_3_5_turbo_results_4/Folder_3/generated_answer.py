
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
        if str(x).count('0') > 0:
            continue
        if not is_prime(x):
            continue

        temp = str(x)
        while len(temp) >= 2:
            temp = temp[1:-1]
            if not is_prime(int(temp)):
                break
        else:
            primes.append(x)

    return sorted(primes)
