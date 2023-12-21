
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for num in numbers:
        if str(num).count('0') == 0 and all([str(num)[i:] != '0' for i in range(1, len(str(num)))]):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
