
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_right_truncatable_prime(numbers: tuple) -> list:
    x = numbers[14]
    right_truncatable_primes = []
    for num in range(x - 1, 9, -1):
        if is_prime(num):
            truncatable = True
            digits = str(num)
            for i in range(len(digits) - 1, 0, -1):
                truncatable = is_prime(int(digits[:i]))
                if not truncatable:
                    break
            if truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
