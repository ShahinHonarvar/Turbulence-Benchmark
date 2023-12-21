
def all_right_truncatable_prime(numbers):
    from sympy import isprime
    
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(isprime(int(str_n[:i])) for i in range(1, len(str_n) + 1))

    x = numbers[41]
    return sorted(num for num in range(2, x) if is_right_truncatable_prime(num))
