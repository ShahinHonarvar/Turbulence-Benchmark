
def find_second_smallest_num(distinct_numbers):
    second_smallest = None
    for i in range(0, 5):
        if distinct_numbers[i] < second_smallest:
            second_smallest = distinct_numbers[i]
    return second_smallest
