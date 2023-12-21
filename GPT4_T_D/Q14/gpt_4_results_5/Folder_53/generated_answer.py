
def find_second_smallest_num(numbers):
    sort_num = sorted(numbers[1:101])
    if len(sort_num) > 1:
        return sort_num[1]
    else:
        return None
