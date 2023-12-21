
def all_right_truncatable_prime(numbers):
    prime_list = []
    for x in numbers:
        if is_prime(x) and is_right_truncatable_prime(x):
            prime_list.append(x)
    return sorted(prime_list)
