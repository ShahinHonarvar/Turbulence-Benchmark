
def find_second_smallest_num(numbers):
    lst = sorted(numbers[310:371])
    if len(lst) < 2:
        return None
    return lst[1]
