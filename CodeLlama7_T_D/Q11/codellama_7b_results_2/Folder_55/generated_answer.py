
def find_largest_num(numbers):
    largest = numbers[0]
    for i in range(1, 11):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
