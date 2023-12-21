
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        str_n = str(n)
        truncate_numbers = []
        for i in range(len(str_n)):
            truncate_numbers.append(int(str_n[i:]))
        return truncate_numbers

    x = numbers[126]
    left_truncatable_primes = []

    for i in range(2, x):
        if '0' not in str(i):
            truncate = truncate_left(i)
            if all(is_prime(num) for num in truncate):
                left_truncatable_primes.append(i)

    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
