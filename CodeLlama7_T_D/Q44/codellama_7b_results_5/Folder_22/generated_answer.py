
def composite_nums_between_indices(my_list):
    # Create a set to store the composite numbers
    composite_nums = set()

    # Loop through the list and check if each number is composite
    for i in range(50, 201):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 50 to 200
    return composite_nums
