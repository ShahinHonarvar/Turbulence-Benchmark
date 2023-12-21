
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[7:10]
    sum = 0
    for n in subset:
        if n % 2 == 0 or n % 3 == 0:
            sum += n
    return sum
