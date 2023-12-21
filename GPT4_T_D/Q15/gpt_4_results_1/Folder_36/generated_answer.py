
def sum_odd_ints_inclusive(int_list):
    return sum(num for index, num in enumerate(int_list[246:751]) if num % 2 != 0)
