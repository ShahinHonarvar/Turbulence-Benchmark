
def find_smallest_num(numbers):
    smallest = numbers[30]
    for num in numbers[31:49]:
        if num < smallest:
            smallest = num
    return smallest
