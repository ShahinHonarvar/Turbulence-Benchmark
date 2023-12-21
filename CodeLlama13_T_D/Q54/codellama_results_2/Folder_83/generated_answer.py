
def all_right_truncatable_prime(numbers):
    x = numbers[24]
    prime_numbers = []
    for i in range(10, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    prime_numbers = [2, 3, 5, 7]
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not is_prime(n) or n in prime_numbers:
            return False
    return True
