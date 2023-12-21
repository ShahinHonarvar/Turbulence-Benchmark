
def find_second_smallest_num(numbers):
    numbers = numbers[55:99]  # slice the list from index 55 to index 98
    numbers = sorted(set(numbers))  # remove duplicates and sort the numbers
    if len(numbers) > 1:
        return numbers[1]  # return the second smallest element
    else:
        return None  # no second smallest element
