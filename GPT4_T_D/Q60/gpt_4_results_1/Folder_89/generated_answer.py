
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    def is_truncatable(num):
        n = str(num)
        return all(is_prime(int(n[i:])) and is_prime(int(n[:i])) for i in range(1, len(n)))

    x = numbers[97]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    return sorted([n for n in primes if '0' not in str(n) and is_truncatable(n)], reverse=True)
