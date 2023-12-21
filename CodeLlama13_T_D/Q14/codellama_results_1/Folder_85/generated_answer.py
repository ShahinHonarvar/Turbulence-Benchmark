
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(6):
        if numbers[i] < numbers[6]:
            second_smallest = numbers[i]
            break
    return second_smallest
