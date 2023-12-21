
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is composite
    for i in range(17, 78 + 1):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers between indices 17 and 78
    return composite_nums
