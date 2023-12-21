
def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    else:
        sub_list = numbers[75:89]
        sub_list.sort()
        return sub_list[-2]
