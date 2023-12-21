
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for num in range(x):
        str_num = str(num)
        if '0' in str_num:
            continue
        else:
            lst_num = list(str_num)
            flag = 1
            while len(lst_num) > 0 and flag == 1:
                if isprime(int("".join(lst_num))):
                    flag = 1
                else:
                    flag = 0
                lst_num.pop(0)
            if flag == 1:
                result.append(int("".join(lst_num)))
    return sorted(result, reverse=True)
