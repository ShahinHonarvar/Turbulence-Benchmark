
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(4):
        if numbers[i] < numbers[3]:
            second_smallest = numbers[i]
            break
    return second_smallest
