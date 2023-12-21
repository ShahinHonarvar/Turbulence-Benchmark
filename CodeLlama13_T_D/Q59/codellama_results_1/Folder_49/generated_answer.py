
def all_left_truncatable_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num) and '0' not in str(num):
            prime_numbers.append(num)
    return sorted(prime_numbers)
