
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(28, 32+1):
        if len(numbers) <= i:
            break
        if second_smallest is None or numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
