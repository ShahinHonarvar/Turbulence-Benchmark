
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[31]
    right_trunc_primes = []

    for i in range(x - 1, 1, -1):
        num = i
        is_right_trunc_prime = True
        while num > 0:
            if not is_prime(num):
                is_right_trunc_prime = False
                break
            num //= 10
        if is_right_trunc_prime:
            right_trunc_primes.append(i)

    return sorted(right_trunc_primes, reverse=True)
