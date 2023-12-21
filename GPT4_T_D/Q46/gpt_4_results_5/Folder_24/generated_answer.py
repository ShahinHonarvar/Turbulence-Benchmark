
def gcf_three_nums(num_list):
    from math import gcd
    if len(num_list) < 44:
        return "List is too small"
    else:
        gcf = gcd(gcd(num_list[18], num_list[37]), num_list[43])
        return gcf
