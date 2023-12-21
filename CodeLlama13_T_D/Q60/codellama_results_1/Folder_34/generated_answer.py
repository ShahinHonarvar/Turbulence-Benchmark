
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and no_zeros(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def no_zeros(n):
    while len(str(n)) > 1:
        if str(n)[0] == '0' or str(n)[-1] == '0':
            n = int(str(n)[:-1])
        else:
            break
    return True
