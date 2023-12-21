
def prime_factors(my_list):
    prime_factors = set()
    for i in range(len(my_list)):
        if is_prime(my_list[i]):
            prime_factors.add(my_list[i])
    return prime_factors

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
