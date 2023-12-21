
def all_left_truncatable_prime(x):
    prime_numbers = []
    for i in range(1, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
