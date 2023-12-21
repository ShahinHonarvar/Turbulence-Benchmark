
def find_second_largest_num(numbers):
    lst = sorted(numbers[639:976])
    return lst[-2] if len(lst) > 1 else None
