
def find_second_smallest_num(numbers):
    sub_list = numbers[64:67]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
