
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_right_truncatable_prime(numbers):
    x = numbers[28]
    truncatable_primes = []

    for num in range(2, x):
        if is_prime(num):
            is_truncatable = True
            digits = list(str(num))

            for i in range(len(digits)-1):
                digits.pop()

                truncatable_num = int("".join(digits))
                if not is_prime(truncatable_num):
                    is_truncatable = False
                    break

            if is_truncatable:
                truncatable_primes.append(num)

    return sorted(truncatable_primes)
