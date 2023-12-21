
def all_ints_not_div_by_num(input_list):
    result=[]
    for num in input_list[2:]:
        if num % -1 != 0:
            result.append(num)
    return result
