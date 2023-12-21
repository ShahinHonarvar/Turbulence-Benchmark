
def find_second_largest_num(numbers):
    if len(numbers) >= 9:
        sub_list = numbers[6:9]
        sub_list.sort()
        return sub_list[-2]
    return None
