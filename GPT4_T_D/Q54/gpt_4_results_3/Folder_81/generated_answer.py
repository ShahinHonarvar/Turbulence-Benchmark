
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[98]
    rtp = []
    for num in range(2, x):
        str_num = str(num)
        is_rtp = all(isprime(int(str_num[:i])) for i in range(1, len(str_num)+1))
        if is_rtp:
            rtp.append(num)
    return sorted(rtp)
