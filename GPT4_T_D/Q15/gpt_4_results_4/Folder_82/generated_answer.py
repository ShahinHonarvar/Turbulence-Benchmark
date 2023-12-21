
def sum_odd_ints_inclusive(int_list):
    int_list = int_list[20:201]
    return sum(num for num in int_list if num % 2 != 0)
