
def all_right_truncatable_prime(n):
    prime_list = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_list.append(i)
    return sorted(prime_list, key=lambda x: x)
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
