
def all_ints_div_by_num(lst):
    result = []
    for num in lst[:3]:
        if num % 9 == 0:
            result.append(num)
    return result
