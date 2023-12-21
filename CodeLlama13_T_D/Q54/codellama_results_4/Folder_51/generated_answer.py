
def all_right_truncatable_prime(tuple):
    x = tuple[54]
    prime_numbers = []
    for i in range(x, 10**5+1):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
