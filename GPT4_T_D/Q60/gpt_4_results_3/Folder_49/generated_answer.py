
def all_left_right_truncatable_prime(tup):
    from sympy import isprime

    # helper function to check truncation
    def is_truncatable(p):
        str_p = str(p)
        len_p = len(str_p)
        if '0' in str_p:
            return False
        for i in range(len_p):
            # remove leftmost and rightmost digits
            left = str_p[i:]
            right = str_p[:len_p - i]
            if not (isprime(int(left)) and isprime(int(right))):
                return False
        return True

    x = tup[14]
    result = []
    for num in range(11, x + 1):
        if isprime(num) and is_truncatable(num):
            result.append(num)
    return sorted(result)
