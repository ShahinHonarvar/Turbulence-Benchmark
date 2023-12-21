
def find_second_largest_num(numbers):
    if len(numbers) < 21:
        return None
    else:
        sublist = numbers[20:201]
        sorted_list = sorted(sublist, reverse=True)
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]
