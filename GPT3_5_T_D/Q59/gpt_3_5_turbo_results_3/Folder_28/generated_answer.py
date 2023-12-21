
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def all_left_truncatable_prime(numbers):

    x = numbers[19]
    truncatable_primes = []
    
    for num in range(10, x):
        if is_prime(num):
            num_str = str(num)
            is_left_truncatable = True

            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_left_truncatable = False
                    break

            if is_left_truncatable:
                truncatable_primes.append(num)

    return sorted(truncatable_primes)
