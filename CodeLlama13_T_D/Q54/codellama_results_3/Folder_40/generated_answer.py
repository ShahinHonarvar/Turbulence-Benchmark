
def all_right_truncatable_prime(numbers):
    x = numbers[10]
    prime_list = []
    for i in range(2,x):
        if is_prime(i) and right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True
