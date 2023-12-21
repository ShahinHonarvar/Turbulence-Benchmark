
def find_second_smallest_num(numbers):
    if len(numbers) < 102:
        return None
    else:
        sort_list = sorted(numbers[1:101])
        return sort_list[1]
