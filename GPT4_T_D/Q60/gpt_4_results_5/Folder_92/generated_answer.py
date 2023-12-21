
def all_left_right_truncatable_prime(t):
    from sympy import isprime

    x = t[7]

    def check(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True

    return sorted([i for i in range(10, x + 1) if check(i)])
