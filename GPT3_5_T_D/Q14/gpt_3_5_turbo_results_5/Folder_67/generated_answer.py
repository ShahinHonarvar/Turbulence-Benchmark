
def find_second_smallest_num(numbers):
    lst = sorted(numbers[50:55])
    if len(lst) < 2:
        return None
    return lst[1]
