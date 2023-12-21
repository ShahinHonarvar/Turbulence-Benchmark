
def all_left_truncatable_prime(numbers):
    from sympy import isprime

    x = numbers[49]

    def is_left_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True

    return sorted(filter(is_left_truncatable_prime, range(2, x)))
