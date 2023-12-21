
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(1, 100+1):
        if numbers[i] < numbers[1]:
            second_smallest = numbers[i]
            break
    return second_smallest
