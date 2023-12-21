
from sympy import isprime

def all_left_right_truncatable_prime(tpl):
    x = tpl[466]
    lst = []
    for num in range(11, x + 1):
        if num < 10 and isprime(num):
            lst.append(num)
        elif '0' not in str(num):
            flg = isprime(num)
            left = right = str(num)
            while len(left) > 1 and flg:
                left, right = left[1:], right[:-1]
                flg = isprime(int(left)) and isprime(int(right))
            if flg:(lst.append(num))
    return sorted(lst, reverse=True)
