
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True

    x = numbers[81]
    truncatable_primes = [i for i in range(2, x+1) if is_prime(i) and is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)
