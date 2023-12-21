
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(1, 8):
        if numbers[i] < numbers[i-1]:
            second_smallest = numbers[i]
            break
    return second_smallest
