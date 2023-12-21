
def find_second_smallest_num(distinct_numbers):
    sorted_list = sorted(distinct_numbers)
    if len(sorted_list[36:47]) < 2:
        return None
    else:
        return sorted_list[36:47][1]
