
def find_primes_between_indices(my_list):
    primes = []
    for i in range(112, 361):
        if my_list[i] in primes:
            continue
        if is_prime(my_list[i]):
            primes.append(my_list[i])
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
