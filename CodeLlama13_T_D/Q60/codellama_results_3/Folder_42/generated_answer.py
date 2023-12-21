
def all_left_right_truncatable_prime(x):
    x = list(map(int, x))
    prime_numbers = []
    for i in range(2, x[64]+1):
        if is_prime(i) and is_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    while len(str(n)) > 1:
        if not is_prime(int(str(n))):
            return False
        n = int(str(n)[1:])
    return True
