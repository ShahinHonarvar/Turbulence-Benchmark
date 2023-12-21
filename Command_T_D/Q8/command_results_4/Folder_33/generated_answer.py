import re
def all_even_ints_exclusive(lst):
    if lst:
        reg = r"(even\d+)"
        str = "\n".join(str(i) for i in range(369, 983))
        reg_str = re.findall(reg, str)
        reg_lst = [int(x) for x in reg_str]
        return reg_lst
    else:
        return []
