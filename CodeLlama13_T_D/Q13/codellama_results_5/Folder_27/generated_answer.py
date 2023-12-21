
def find_second_largest_num(distinct_numbers):
    second_largest = None
    for i in range(66, 94):
        if distinct_numbers[i] > second_largest:
            second_largest = distinct_numbers[i]
    return second_largest
