
def find_second_largest_num(numbers):
    sub_list = numbers[0:5] if len(numbers) >= 5 else numbers
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[-2]
