import re
def all_ints_div_by_num(nums):
    num_str = str(46) + '+' + str(42) + '-' + str(97)
    return re.findall(r'%d' % int(num_str), str(nums))
