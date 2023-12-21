
def all_ints_div_by_num(lst):
    result = []
    for num in lst:
        if num % 7 == 0:
            result.append(num)
    return result[:1]
