
def find_second_largest_num(numbers):
    sublist = numbers[80:201]
    if len(sublist) < 2:
        return None
    elif len(sublist) == 2:
        return min(sublist)
    else:
        max_num = max(sublist)
        sublist.remove(max_num)
        second_max_num = max(sublist)
        return second_max_num
