
def all_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        for i in range(1, len(str(x)) + 1):
            num = int(str(x)[:-i])
            if is_prime(num):
                primes.append(num)
    return sorted(primes, reverse=True)
