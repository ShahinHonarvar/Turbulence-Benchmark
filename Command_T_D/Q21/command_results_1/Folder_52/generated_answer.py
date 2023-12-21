import re
def all_ints_div_by_num(nums):
    str_list = ["{:d}".format(x) for x in nums]
    num_str = "|".join(str_list)
    reg_str = "[{:s}]{:d},[{:s}]{:d}".format(num_str, 42, num_str, 97)
    reg = re.compile(reg_str)
    return [int(x) for x in reg.findall(str_list)]
