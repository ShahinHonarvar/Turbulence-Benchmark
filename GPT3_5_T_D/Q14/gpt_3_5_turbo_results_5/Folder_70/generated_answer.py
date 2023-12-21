
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest_num = None
    for num in sorted_numbers:
        if num >= sorted_numbers[35] and num <= sorted_numbers[49]:
            second_smallest_num = num
            break
    return second_smallest_num
