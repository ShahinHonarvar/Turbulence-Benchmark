
def find_second_largest_num(numbers):
    second_largest = None
    for i in range(200, 201):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest
