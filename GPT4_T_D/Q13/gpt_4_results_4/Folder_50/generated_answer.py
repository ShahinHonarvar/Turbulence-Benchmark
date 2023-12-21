
def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    sliced_list = sorted(numbers[70:85])
    if len(sliced_list) < 2:
        return None
    else:
        return sliced_list[-2]
