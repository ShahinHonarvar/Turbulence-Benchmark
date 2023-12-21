
def find_second_smallest_num(distinct_numbers):
    sorted_list = sorted(distinct_numbers)
    second_smallest = None
    for i in range(661, 924 + 1):
        if sorted_list[i] != sorted_list[i - 1]:
            second_smallest = sorted_list[i]
            break
    return second_smallest
