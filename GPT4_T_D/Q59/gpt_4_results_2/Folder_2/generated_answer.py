
def all_left_truncatable_prime(numbers):
    from sympy import isprime

    x = numbers[618]
    def is_left_truncatable_prime(n):
        
        s = str(n)

        if '0' in s:
            return False

        return all(isprime(int(s[i:])) for i in range(len(s)))

    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
