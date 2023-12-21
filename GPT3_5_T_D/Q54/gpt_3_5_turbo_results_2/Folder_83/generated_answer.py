
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_right_truncatable_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            is_right_truncatable = True
            temp = str(i)
            while temp:
                if not is_prime(int(temp)):
                    is_right_truncatable = False
                    break
                temp = temp[:-1]
            if is_right_truncatable:
                primes.append(i)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[24]
    primes = get_right_truncatable_primes(x)
    return sorted(primes)
