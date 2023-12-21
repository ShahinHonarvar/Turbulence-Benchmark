
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers[:976]:
        if '0' not in str(x) and is_prime(x):
            truncate_prime = True
            for i in range(1, len(str(x))):
                if not is_prime(int(str(x)[i:])) or not is_prime(int(str(x)[:-i])):
                    truncate_prime = False
                    break
            if truncate_prime:
                primes.append(x)
    return sorted(primes, reverse=True)
