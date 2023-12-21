
def find_second_largest_num(distinct_numbers):
    if len(distinct_numbers) < 2:
        return None
    second_largest = distinct_numbers[1]
    for num in distinct_numbers[2:]:
        if num > second_largest:
            second_largest = num
    return second_largest
