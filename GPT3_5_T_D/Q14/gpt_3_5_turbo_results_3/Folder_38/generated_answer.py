
def find_second_smallest_num(numbers):
    selection = sorted(numbers[37:52])
    if len(selection) >= 2:
        return selection[1]
    else:
        return None
