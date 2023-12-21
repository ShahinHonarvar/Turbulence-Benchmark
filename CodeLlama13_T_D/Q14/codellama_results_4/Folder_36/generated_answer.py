
def find_second_smallest_num(distinct_numbers):
    second_smallest = None
    for i in range(209, 556+1):
        if distinct_numbers[i] < distinct_numbers[i-1]:
            second_smallest = distinct_numbers[i]
    return second_smallest
