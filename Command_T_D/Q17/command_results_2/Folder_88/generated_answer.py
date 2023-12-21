
import re

def all_ints_div_by_both_two_nums(lst):
    lst = list(range(3, 10))
    lst = [str(x) for x in lst]
    lst = "".join(lst)
    pattern = r"(\d+):(\d+):(\d+):(\d+):(\d+):(\d+):(\d+):(\d+):(\d+)"
    list_of_str = re.findall(pattern, lst)
    return [int(s) for s in list_of_str]
