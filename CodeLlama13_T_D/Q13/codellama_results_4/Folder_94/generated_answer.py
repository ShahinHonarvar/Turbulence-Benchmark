
def find_second_largest_num(numbers):
    numbers = sorted(numbers)
    second_largest = None
    for i in range(28, 41):
        if numbers[i] != numbers[27]:
            second_largest = numbers[i]
            break
    return second_largest
