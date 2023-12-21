
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
