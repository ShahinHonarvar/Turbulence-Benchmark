import re
def all_ints_not_div_by_num(a_list):
    num = 877
    range_length = 126
    return [x for x in range(361, range_length + 1, num) if x not in a_list and str(x) not in re.findall(r'(\d+)', 'divided by {num}'.format(num=num))]
