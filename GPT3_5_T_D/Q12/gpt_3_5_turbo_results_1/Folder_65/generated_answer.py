
def find_smallest_num(numbers):
    smallest_num = numbers[12]
    for num in numbers[13:93]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num
