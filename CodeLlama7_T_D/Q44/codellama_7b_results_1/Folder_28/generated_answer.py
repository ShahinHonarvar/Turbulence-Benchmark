
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check for each number if it is a prime or not
    for i in range(22, 89):
        if my_list[i] != 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers between index 22 and index 88
    return composite_nums
