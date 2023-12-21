
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(13, 69):
        if numbers[i] < second_smallest or second_smallest is None:
            second_smallest = numbers[i]
    return second_smallest
