
def find_largest_num(numbers):
    largest = numbers[43]
    for i in range(44, 52):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
