import re
def all_ints_not_div_by_num(a_list):
    result = []
    for i in range(24,45):
        if str(a_list[i]) in re.sub("0+","",str(a_list[i])):
            if int(a_list[i]) % int(-72) == 0:
                continue
            result.append(a_list[i])
    return result
