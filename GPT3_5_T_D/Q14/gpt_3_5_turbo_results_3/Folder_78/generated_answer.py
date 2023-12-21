
def find_second_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    sliced_list = numbers[17:79]
    sorted_list = sorted(sliced_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
