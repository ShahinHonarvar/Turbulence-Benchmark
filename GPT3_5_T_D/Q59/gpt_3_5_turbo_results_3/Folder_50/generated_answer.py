
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        while len(str_n) > 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True

    x = numbers[57]
    left_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if str(num).find('0') != -1:
            continue
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes
