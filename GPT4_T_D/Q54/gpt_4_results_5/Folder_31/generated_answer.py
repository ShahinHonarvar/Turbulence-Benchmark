
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
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

    x = numbers[50]
    truncatable_primes = []
    for i in range(x):
        if is_prime(i) and is_truncatable(i):
            truncatable_primes.append(i)

    truncatable_primes.sort(reverse=True)
    return truncatable_primes
