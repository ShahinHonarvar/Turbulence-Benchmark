import re
def all_ints_not_div_by_num(x):
    z = []
    for i in range(767, 938):
        if str(i) not in re.findall(r'([13579])?([234789])?([13579])?', str(x)):
            z.append(i)
    return z
