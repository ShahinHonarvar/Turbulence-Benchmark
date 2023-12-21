
def sum_odd_ints_inclusive(int_list):
    sub_list = int_list[15:40]
    odd_ints = [num for num in sub_list if num % 2 != 0]
    return sum(odd_ints) if odd_ints else 0
