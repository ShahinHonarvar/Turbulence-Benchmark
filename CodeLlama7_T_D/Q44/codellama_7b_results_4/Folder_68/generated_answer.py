
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # If the current number is a prime number, check if it is between index 0 and index 8
        if my_list[i] > 1:
            for j in range(9):
                # If the current number is divisible by any number between 2 and the square root of the current number, it is not prime
                if my_list[i] % (j + 1) == 0:
                    break
            else:
                # If the loop completes without breaking, the current number is a prime number
                composite_nums.add(my_list[i])

    return composite_nums
