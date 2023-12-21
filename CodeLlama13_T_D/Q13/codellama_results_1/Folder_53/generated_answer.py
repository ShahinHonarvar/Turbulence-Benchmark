
def find_second_largest_num(numbers):
    largest = None
    second_largest = None
    for num in numbers[100:200]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
