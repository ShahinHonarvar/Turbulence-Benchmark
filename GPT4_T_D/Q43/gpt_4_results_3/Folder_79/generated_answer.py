
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(int_list):
    primes = []
    for i in range(33, 36):
        if i < len(int_list) and is_prime(int_list[i]):
            primes.append(int_list[i])
    return sorted(primes)
