
def find_second_smallest_num(numbers):
    if len(numbers) < 81:
        return None
    sublist = numbers[40:81]
    sorted_list = sorted(set(sublist))
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
