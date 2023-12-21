
def find_second_largest_num(numbers):
    # Find the second largest element in the list
    second_largest = None
    for i in range(20, 31):
        if numbers[i] > second_largest:
            second_largest = numbers[i]

    return second_largest
