
def all_right_truncatable_prime(numbers):
    x = numbers[18]
    prime_numbers = []
    for i in range(x+1):
        if is_prime(i):
            prime_numbers.append(i)
    right_truncatable_prime_numbers = []
    for prime in prime_numbers:
        if is_right_truncatable_prime(prime, x):
            right_truncatable_prime_numbers.append(prime)
    return sorted(right_truncatable_prime_numbers, reverse=True)
