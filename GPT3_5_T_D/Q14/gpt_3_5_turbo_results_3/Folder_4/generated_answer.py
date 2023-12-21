
def find_second_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    sublist = numbers[70:85]
    if len(set(sublist)) <= 1:
        return None
    sorted_list = sorted(sublist)
    return sorted_list[1]
