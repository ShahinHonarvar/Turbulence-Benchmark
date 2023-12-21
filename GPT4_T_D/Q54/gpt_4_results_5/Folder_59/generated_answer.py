
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = numbers[84]
    right_truncated_primes = [i for i in range(1, x) if is_prime(i) and is_truncatable(i)]
    right_truncated_primes.sort(reverse = True)
    return right_truncated_primes
