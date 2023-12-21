
from math import gcd

def gcf_three_nums(lst):
    if not isinstance(lst, list) or len(lst)<95 or not all(isinstance(i, int) and i>0 for i in lst):
        return 'Please provide a valid input'

    return gcd(gcd(lst[19], lst[94]), lst[78])
