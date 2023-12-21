
def find_second_smallest_num(distinct_numbers):
    second_smallest = None
    for i in range(62, 64):
        if distinct_numbers[i] < distinct_numbers[63]:
            second_smallest = distinct_numbers[i]
    return second_smallest
