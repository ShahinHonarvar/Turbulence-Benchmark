
def find_second_largest_num(numbers):
    num_list = numbers[22:51]
    num_list.sort()
    if len(num_list) >= 2:
        return num_list[-2]
    else:
        return None
