
def find_primes_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for index, number in enumerate(numbers[21:98]):
        if is_prime(number):
            primes.append(number)

    return sorted(primes)
