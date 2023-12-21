
def sum_ints_div_by_either_nums(list_of_ints):
    sum_values = 0
    for num in list_of_ints[11:77]:
        if num % -81 == 0 or num % -94 == 0:
            sum_values += num
    return sum_values
