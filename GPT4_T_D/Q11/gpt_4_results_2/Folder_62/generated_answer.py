
def find_largest_num(numbers):
    if len(numbers)>=100:
        return max(numbers[91:100])
    else:
        return "The list doesn't contain at least 100 elements"
