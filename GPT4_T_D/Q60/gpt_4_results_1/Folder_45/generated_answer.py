
def all_left_right_truncatable_prime(numbers):
    import sympy

    def check_num(num):
        str_num = str(num)
        if "0" in str_num:
            return False
        for i in range(len(str_num)):
            left_num = str_num[i:]
            right_num = str_num[:len(str_num) - i]
            if not(sympy.isprime(int(left_num)) and sympy.isprime(int(right_num))):
                return False
        return True

    x = numbers[61]
    prime_numbers = [n for n in range(10, x + 1) if sympy.isprime(n)]
    result = [n for n in prime_numbers if check_num(n)]
    result.sort()
    return result
