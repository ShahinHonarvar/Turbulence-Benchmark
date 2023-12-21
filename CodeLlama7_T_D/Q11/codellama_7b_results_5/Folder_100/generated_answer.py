
def find_largest_num(numbers):
    largest = numbers[42]
    for i in range(43, 69):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
