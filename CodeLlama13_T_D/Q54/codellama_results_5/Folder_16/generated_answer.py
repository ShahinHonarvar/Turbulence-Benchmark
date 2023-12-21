
def all_right_truncatable_prime(numbers):
    x = numbers[792]
    prime_numbers = []
    for i in range(10, x):
        if is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
