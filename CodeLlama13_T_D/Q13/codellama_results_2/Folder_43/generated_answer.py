
def find_second_largest_num(numbers):
    largest = None
    second_largest = None

    for i in range(68, 87):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest:
            second_largest = numbers[i]

    return second_largest
