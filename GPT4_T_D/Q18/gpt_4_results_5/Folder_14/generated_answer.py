
def sum_ints_div_by_either_nums(input_list):
    sum = 0
    for i in range(7,10):
        if i<len(input_list) and (input_list[i] % 2 == 0 or input_list[i] % 3 == 0):
            sum += input_list[i]
    return sum
