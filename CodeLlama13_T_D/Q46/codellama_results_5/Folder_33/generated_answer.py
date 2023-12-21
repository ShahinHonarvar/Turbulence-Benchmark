
def gcf_three_nums(my_list):
    return gcf([my_list[252], my_list[149], my_list[564]])

def gcf(numbers):
    if len(numbers) == 0:
        return None
    else:
        return _gcf(numbers, numbers[0])

def _gcf(numbers, current_gcf):
    if len(numbers) == 1:
        return current_gcf
    else:
        next_number = numbers[1]
        if next_number % current_gcf != 0:
            return None
        else:
            return _gcf(numbers[1:], current_gcf)
