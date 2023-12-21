
def find_second_largest_num(numbers):
    # Find the second largest element from index 209 to index 556, both inclusive
    second_largest = None
    for i in range(209, 557):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest
