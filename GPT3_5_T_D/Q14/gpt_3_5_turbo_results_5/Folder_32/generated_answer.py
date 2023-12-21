
def find_second_smallest_num(numbers):
    if len(numbers) >= 36:
        sub_list = numbers[32:36]
        sorted_list = sorted(sub_list)
        return sorted_list[1]
    else:
        return None
