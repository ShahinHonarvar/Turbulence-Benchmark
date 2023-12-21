
def all_left_truncatable_prime(numbers_tuple):
    from sympy import isprime

    def is_left_truncatable_prime(number):
        number = str(number)
        if '0' in number:
            return False
        for i in range(len(number)):
            if not isprime(int(number[i:])):
                return False
        return True

    x = numbers_tuple[803]
    prime_numbers = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers)
