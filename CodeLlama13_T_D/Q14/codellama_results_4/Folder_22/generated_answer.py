
def find_second_smallest_num(numbers):
    sorted_list = sorted(numbers)
    for i in range(40, 201):
        if sorted_list[i] != sorted_list[i - 1]:
            return sorted_list[i]
    return None
