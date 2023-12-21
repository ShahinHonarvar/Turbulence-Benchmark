
import math

def gcf_three_nums(lst):
    if len(lst) >= 99:
        return math.gcd(math.gcd(lst[70], lst[98]), lst[22])
    else:
        return 'Insufficient length.'
