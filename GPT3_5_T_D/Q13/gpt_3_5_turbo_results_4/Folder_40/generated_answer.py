
def find_second_largest_num(numbers):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)

    # If there are at least 3 numbers in the list, return the second element
    if len(numbers) >= 3:
        return numbers[1]
    else:
        return None
