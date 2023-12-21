
def find_second_smallest_num(numbers):
    sublist = numbers[246:751]
    if len(sublist) <= 1:
        return None
    else:
        sorted_sublist = sorted(set(sublist))
        return sorted_sublist[1]
