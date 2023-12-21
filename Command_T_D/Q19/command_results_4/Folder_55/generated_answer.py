import re
def all_ints_not_div_by_num(int_list):
    result = re.findall(r'(\d+)', str(int_list))
    if result:
        return [int(i) for i in result if int(i) % 10 != 0]
    else:
        return []
