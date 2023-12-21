
def find_second_largest_num(numbers):
    largest = 0
    second_largest = 0
    for i in range(6, 9):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
    return second_largest
