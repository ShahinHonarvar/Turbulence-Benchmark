
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_two_digit_prime(n):
        return n in [2, 3, 5, 7]

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if not is_two_digit_prime(int(s[i:])) or not is_two_digit_prime(int(s[:-i])):
                return False
        return True

    x = numbers[370]
    primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)

    return sorted(primes, reverse=True)
