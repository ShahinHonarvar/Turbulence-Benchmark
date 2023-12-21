
def find_largest_num(numbers):
    largest = numbers[19]
    for i in range(20, 93):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
