
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n, primes):
        if n < 10:
            return True
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            left_num = int(n_str[i:])
            if left_num not in primes:
                return False
            right_num = int(n_str[:i])
            if right_num not in primes:
                return False
        return True

    primes = [i for i in range(2, max(numbers) + 1) if is_prime(i)]
    result = [x for x in primes if x <= numbers[630] and is_left_right_truncatable_prime(x, primes)]
    return sorted(result, reverse=True)
