
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 25 to index 87, both inclusive
    for i in range(25, 88):

        # If the current element is a prime number, add it to the set of composite numbers
        if my_list[i] == 1:
            composite_nums.add(my_list[i])

        # If the current element is not a prime number, check if it is a composite number
        else:

            # Check if the current element is a power of 2 or a Mersenne prime
            for j in range(1, int(math.log(my_list[i], 2)) + 1)):
                if my_list[i] == 2 ** j - 1:
                    composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 25 to index 87, both inclusive
    return composite_nums
