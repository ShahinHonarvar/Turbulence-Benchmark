
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers starting from index 90 (inclusive) and ending at index 200 (exclusive)
    for i in range(90, 200):

        # Check if the current element is even and store it in a temporary variable 'x'

        x = my_list[i]

        if x % 2 == 0:

            # If the current element is even, add it to the list of even integers

            even_ints.append(x)

    return even_ints
