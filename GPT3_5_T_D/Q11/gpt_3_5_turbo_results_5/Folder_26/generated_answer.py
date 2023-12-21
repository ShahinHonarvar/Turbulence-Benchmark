
def find_largest_num(numbers):
    largest = numbers[62]
    for i in range(62, 100):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
