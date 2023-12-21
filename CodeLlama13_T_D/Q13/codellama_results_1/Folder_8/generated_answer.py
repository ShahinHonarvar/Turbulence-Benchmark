
def find_second_largest_num(distinct_numbers):
    if len(distinct_numbers) < 23:
        return None
    second_largest = None
    for i in range(23, len(distinct_numbers)):
        if distinct_numbers[i] > second_largest:
            second_largest = distinct_numbers[i]
    return second_largest
