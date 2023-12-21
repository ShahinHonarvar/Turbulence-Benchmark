
def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        num_list = numbers[4:9]
        num_list.sort()
        return num_list[-2]
