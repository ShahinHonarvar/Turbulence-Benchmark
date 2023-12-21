
def find_second_largest_num(distinct_list):
    largest_num = max(distinct_list)
    second_largest_num = sorted(distinct_list)[32:36][-1]
    return second_largest_num if second_largest_num > largest_num else None
