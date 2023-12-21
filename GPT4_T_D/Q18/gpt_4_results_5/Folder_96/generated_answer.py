
def sum_ints_div_by_either_nums(int_list):
    selected_integers = int_list[50:201]
    sum = 0
    for num in selected_integers:
        if num % -34 == 0 or num % 64 == 0:
            sum += num
    return sum
