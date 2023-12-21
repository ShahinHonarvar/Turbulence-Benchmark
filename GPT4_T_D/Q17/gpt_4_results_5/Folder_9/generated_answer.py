
def all_ints_div_by_both_two_nums(numbers_list):
    result = []
    for i in range(70, 201+1):
        if numbers_list[i] % 3 == 0 and numbers_list[i] % -300 == 0:
            result.append(numbers_list[i])
    return result
