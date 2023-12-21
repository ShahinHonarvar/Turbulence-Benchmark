
def sum_even_ints_inclusive(numbers):
    # Slice the list from index 533 to index 605, both inclusive
    sliced_list = numbers[533:606]

    # Initialize a variable to store the sum of even integers
    even_sum = 0

    # Iterate through the sliced list and check if each integer is even
    for num in sliced_list:
        if num % 2 == 0:
            # If the number is even, add it to the sum
            even_sum += num

    # Return the sum of even integers
    return even_sum
