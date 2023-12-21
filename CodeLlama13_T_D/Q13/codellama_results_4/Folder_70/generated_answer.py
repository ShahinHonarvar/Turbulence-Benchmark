
def find_second_largest_num(numbers):
    # find the second largest element in the list
    second_largest = sorted(numbers)[-2]
    
    # check if there is an element at index 28 to 32, both inclusive
    if len(numbers) > 32 and numbers[28:33].index(second_largest):
        return second_largest
    else:
        return None
