
def all_ints_div_by_both_two_nums(integers):
    result = []
    for num in integers[250:630]:
        if num % 850 == 0 and num % 587 == 0:
            result.append(num)
    return result
