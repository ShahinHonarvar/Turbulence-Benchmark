
def find_second_largest_num(numbers):
    largest = None
    second_largest = None
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
