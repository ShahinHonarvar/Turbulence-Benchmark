
def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    else:
        sorted_sub_list = sorted(numbers[56:58])
        if len(sorted_sub_list) > 1:
            return sorted_sub_list[1]
        else:
            return None
