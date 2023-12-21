
def sum_ints_div_by_either_nums(input_list):
    sublist = input_list[61:89]
    sum = 0
    for num in sublist:
        if num % 31 == 0 or num % 11 == 0:
            sum += num
    return sum
