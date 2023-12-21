
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    truncatables = []
    for i in range(11, x+1):
        if '0' in str(i):
            continue
        str_i = str(i)
        for j in range(len(str_i)):
            left_trunc = int(str_i[j:])
            right_trunc = int(str_i[:len(str_i)-j])
            if not (isprime(left_trunc) and isprime(right_trunc)):
                break
        else:
            truncatables.append(i)
    truncatables.sort(reverse=True)
    return truncatables
