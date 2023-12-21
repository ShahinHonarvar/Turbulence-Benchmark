
import re

def all_left_right_truncatable_prime(test_case):
    # enter your code here. read input from STDIN. write output to STDOUT
    res = []
    for n in range(10, int(test_case[0])+1):
        s = str(n)
        if re.fullmatch(r'(\d++){5}\1', s):
            res.append(int(n))
    return res
