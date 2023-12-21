
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if '0' not in str(n) and is_prime(n):
            n_str = str(n)
            while len(n_str) > 1:
                if not is_prime(int(n_str)):
                    break
                n_str = n_str[1:-1]
            else:
                primes.append(n)
    return sorted(primes)
