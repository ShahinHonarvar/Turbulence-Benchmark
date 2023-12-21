import re
def all_ints_not_div_by_num(nums):
    all_ints = list(range(19,70))
    for i in all_ints:
        if str(i) in re.findall(r'(^97|97$)', str(i)):
            all_ints.remove(i)
    return all_ints
