
def find_second_smallest_num(numbers):
    sorted_list = sorted(numbers[29:80])
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
