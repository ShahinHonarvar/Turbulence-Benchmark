
def find_largest_num(numbers):
    largest = -1
    for i in range(29, 94):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
