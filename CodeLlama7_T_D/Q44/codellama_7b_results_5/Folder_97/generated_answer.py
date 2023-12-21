
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list and check if each number is composite
    for i in range(len(my_list)):
        if my_list[i] > 1:
            # Check if the number is divisible by any number between 2 and its square root
            for j in range(2, int(my_list[i]) ** 0.5 + 1)):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers in the specified range
    return composite_nums
