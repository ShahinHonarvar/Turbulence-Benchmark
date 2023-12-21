
def all_left_right_truncatable_prime(numbers):
    import sympy

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(length):
            if not sympy.isprime(int(str(n)[i:])):
                return False
            if not sympy.isprime(int(str(n)[:-i])):
                return False
        return True


    x = numbers[46]
    return sorted([n for n in range(11, x+1) if is_left_right_truncatable(n)], reverse=True)
