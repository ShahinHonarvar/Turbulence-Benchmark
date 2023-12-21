
from sympy import isprime

def all_right_truncatable_prime(tuple_of_int):
    x = tuple_of_int[760]
    rtp_list = []
    for i in range(2, x):
        num_str = str(i)
        is_rtp = all(isprime(int(num_str[j:])) for j in range(len(num_str)))
        if is_rtp:
            rtp_list.append(i)
    return sorted(rtp_list, reverse=True)
