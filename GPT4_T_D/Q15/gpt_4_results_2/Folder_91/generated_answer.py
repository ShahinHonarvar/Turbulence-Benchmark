
def sum_odd_ints_inclusive(lst):
    selected_nums = lst[0:6]
    return sum(num for num in selected_nums if num % 2 != 0)
