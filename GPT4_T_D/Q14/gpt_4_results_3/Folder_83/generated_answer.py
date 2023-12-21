
def find_second_smallest_num(list_of_numbers):
    try:
        sorted_list = sorted(list_of_numbers[90:201])
        if len(sorted_list) < 2:
            return None
        return sorted_list[1]
    except Exception as e:
        return None
