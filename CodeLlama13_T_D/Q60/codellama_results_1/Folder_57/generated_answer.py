
def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def contains_zero(n):
    while n > 0:
        if n % 10 == 0:
            return True
        n //= 10
    return False
