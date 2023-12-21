
def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    else:
        sub_list = numbers[91:100]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[1]
        else:
            return None
