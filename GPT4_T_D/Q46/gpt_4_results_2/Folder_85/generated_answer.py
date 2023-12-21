
import math
def gcf_three_nums(num_list):
    a = num_list[49]
    b = num_list[46]
    c = num_list[13]

    def gcf(a, b):
        return math.gcd(a, b)

    return gcf(gcf(a,b),c)
