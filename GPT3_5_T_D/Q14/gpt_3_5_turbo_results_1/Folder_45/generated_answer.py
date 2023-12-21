
def find_second_smallest_num(numbers):
    sublist = numbers[30:201]
    if len(set(sublist)) > 1:
        return sorted(set(sublist))[1]
    else:
        return None
