
def find_second_smallest_num(numbers):
    sub_list = numbers[40:81]
    if len(sub_list) < 2:
        return None
    else:
        return sorted(sub_list)[1]
