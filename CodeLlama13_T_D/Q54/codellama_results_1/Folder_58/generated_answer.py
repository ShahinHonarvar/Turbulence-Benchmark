
def all_right_truncatable_prime(numbers):
    prime_list = []
    for num in numbers:
        if is_prime(num) and is_right_truncatable_prime(num):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True
