
def find_second_smallest_num(numbers):
    if len(numbers) < 30:
        return None
    else:
        sliced_list = numbers[29:80]
        sliced_list.sort()
        if len(sliced_list) < 2:
            return None
        else:
            return sliced_list[1]
