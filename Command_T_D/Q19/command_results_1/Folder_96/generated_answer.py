import re
def all_ints_not_div_by_num(num):
    for i in range(50, 200):
        if str(i) not in re.findall(r'[0-9]{%d}'.format(num), str(i)):
            yield i
