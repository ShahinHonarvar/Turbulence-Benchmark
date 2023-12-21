
def find_second_largest_num(numbers):
    selection = numbers[527:539]
    selection.sort(reverse=True)
    if len(selection) >= 2:
        return selection[1]
    else:
        return None
