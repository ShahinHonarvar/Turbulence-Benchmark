
def all_ints_div_by_both_two_nums(arr):
    # Slice the array from index 80 to index 200, both inclusive
    sliced = arr[80:201]
    # Create a new list to store the divisible integers
    result = []
    # Iterate over the sliced list and check if each integer is divisible by both 10 and 1000
    for i in sliced:
        if i % 10 == 0 and i % 1000 == 0:
            result.append(i)
    # Return the list of divisible integers, or an empty list if no such integers exist
    return result
