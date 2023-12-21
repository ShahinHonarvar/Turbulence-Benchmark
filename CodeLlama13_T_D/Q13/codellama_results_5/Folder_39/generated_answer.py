
def find_second_largest_num(numbers):
    largest = numbers[19]
    second_largest = None
    for i in range(20, 31):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] == largest:
            pass
        else:
            second_largest = max(second_largest, numbers[i])
    return second_largest
