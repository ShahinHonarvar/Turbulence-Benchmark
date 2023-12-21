
def find_second_largest_num(distinct_numbers):
    if len(distinct_numbers[1:6]) < 2:
        return None
    else:
        sorted_list = sorted(distinct_numbers[1:6])
        return sorted_list[-2]
