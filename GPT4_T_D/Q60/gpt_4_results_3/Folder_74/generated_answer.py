
def all_left_right_truncatable_prime(numbers):
    x = numbers[36]

    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not check_prime(int(str(n)[i:])) or not check_prime(int(str(n)[:-i-1])):
                return False
        return True

    truncatable_primes = [i for i in range(10, x + 1) if check_prime(i) and check_truncatable(i)]
    return sorted(truncatable_primes)
