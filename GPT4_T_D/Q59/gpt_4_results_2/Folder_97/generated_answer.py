
def all_left_truncatable_prime(numbers):
    import sympy
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all(sympy.isprime(int(str_n[i:])) for i in range(len(str_n)))
        
    x = numbers[645]
    lst_prime = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(lst_prime)
