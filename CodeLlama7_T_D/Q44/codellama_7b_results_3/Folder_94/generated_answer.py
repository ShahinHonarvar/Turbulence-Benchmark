
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is a composite number
    for i in range(27, 56):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 27 and 55
    return composite_nums
