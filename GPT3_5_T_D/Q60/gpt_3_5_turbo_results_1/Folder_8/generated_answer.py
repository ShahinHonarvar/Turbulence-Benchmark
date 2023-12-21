
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
        if x < 10 or x % 10 == 0:
            continue
        truncatable_prime = True
        str_x = str(x)
        while len(str_x) > 1 and truncatable_prime:
            if not is_prime(int(str_x)):
                truncatable_prime = False
            else:
                str_x = str_x[1:-1]
        if is_prime(int(str_x)) and truncatable_prime:
            primes.append(x)
    return sorted(primes, reverse=True)
