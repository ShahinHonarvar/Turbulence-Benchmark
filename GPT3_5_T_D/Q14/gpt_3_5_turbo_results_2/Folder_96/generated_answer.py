
def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sorted_list = sorted(numbers[50:201])
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
