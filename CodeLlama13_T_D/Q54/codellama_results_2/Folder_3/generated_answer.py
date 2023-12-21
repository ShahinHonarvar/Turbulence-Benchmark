
def all_right_truncatable_prime(numbers):
    x = numbers[100]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
