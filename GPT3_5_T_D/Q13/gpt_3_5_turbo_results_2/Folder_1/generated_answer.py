
def find_second_largest_num(numbers):
    numbers = numbers[31:73]
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    return numbers[1]
