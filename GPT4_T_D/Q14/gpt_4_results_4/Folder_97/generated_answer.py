
def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    else:
        sublist = sorted(numbers[31:35])
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]
