
def find_second_largest_num(numbers):
    if len(numbers) >= 79:
        sub_list = numbers[62:79]
        sub_list.sort()
        return sub_list[-2]
    else:
        return None
