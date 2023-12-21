
def all_left_right_truncatable_prime(numbers):
    left_and_right_truncatable_primes = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            left_and_right_truncatable_primes.append(num)
    return sorted(left_and_right_truncatable_primes)
