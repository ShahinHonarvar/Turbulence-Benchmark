
def find_second_smallest_num(numbers):
    num_list = numbers[62:100]
    if len(num_list)<2:
        return None
    else:
        num_list.sort()
        return num_list[1]
