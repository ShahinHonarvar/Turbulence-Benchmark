
def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    second_largest = sorted(numbers)[5]
    for num in numbers[6:]:
        if num > second_largest:
            second_largest = num
    return second_largest
