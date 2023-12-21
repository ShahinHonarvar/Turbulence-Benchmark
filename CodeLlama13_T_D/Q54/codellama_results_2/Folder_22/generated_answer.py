
def all_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        prime = True
        while len(str(x)) > 1:
            if not is_prime(x % 10):
                prime = False
                break
            x //= 10
        if prime:
            primes.append(x)
    return sorted(primes)
