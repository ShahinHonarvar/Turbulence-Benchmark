
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and '0' not in str(num):
            primes.append(num)
    return primes
