
def find_second_largest_num(numbers):
    largest = 0
    second_largest = None
    for i in range(74, 96):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] < largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest
