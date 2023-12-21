
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(10**5, x+1):
        if is_prime(i) and all(is_prime(i // 10**j) for j in range(1, 6)):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
