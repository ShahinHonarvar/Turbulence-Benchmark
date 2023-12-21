import re
def all_even_ints_exclusive(nums):
    lst = re.findall(r"(\\d+)", "743\\d+,?866\\d+")
    return [int(i) for i in lst if i.isdigit()]
