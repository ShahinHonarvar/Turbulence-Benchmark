
def find_second_smallest_num(distinct_list):
    second_smallest = None
    for i in range(62, 93):
        if distinct_list[i] < distinct_list[i-1]:
            if second_smallest is not None:
                return second_smallest
            else:
                second_smallest = distinct_list[i]
    return second_smallest
