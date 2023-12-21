
def find_primes_between_indices(my_list):
    return sorted([x for x in my_list[413:449] if is_prime(x)])

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
