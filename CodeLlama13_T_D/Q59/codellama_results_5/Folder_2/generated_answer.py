
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for num in numbers:
        if str(num).count('0') == 0 and is_prime(num) and all(is_prime(int(str(num)[1:])) for i in range(len(str(num))-1)):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
