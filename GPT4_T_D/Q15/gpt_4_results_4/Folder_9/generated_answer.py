
def sum_odd_ints_inclusive(int_list):
    return sum(num for i, num in enumerate(int_list[70:201]) if num % 2 != 0)
