
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers from index 20 to index 200, both inclusive
    for i in range(20, 201):
        # Check if the current number is a prime number
        if my_list[i] == 1:
            continue

        # Iterate over the list of prime numbers from index 2 to index i-1, both inclusive
        for j in range(2, i):
            # If the current number is divisible by any prime number from index 2 to index j-1, both inclusive, then it is not a prime number and we can break out of the loop
            if my_list[i] % my_list[j] == 0:
                break

        # If the current number has reached the end of the loop without being divided by any prime number from index 2 to index j-1, both inclusive, then it is a prime number and we can add it to the set of composite numbers
        else:
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 20 to index 200, both inclusive
    return composite_numbers
