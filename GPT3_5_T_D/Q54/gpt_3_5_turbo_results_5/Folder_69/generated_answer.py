
def all_right_truncatable_prime(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    right_truncatable_primes = []
    x = numbers[760]
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            test_number = i
            while test_number > 0:
                if not is_prime(test_number):
                    is_right_truncatable = False
                    break
                test_number //= 10
            if is_right_truncatable:
                right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes, reverse=True)
