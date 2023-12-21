
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            trunc_num = int(str_n[i:])
            if not is_prime(trunc_num):
                return False
        return True

    x = numbers[55]
    left_trunc_primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes, reverse=True)
