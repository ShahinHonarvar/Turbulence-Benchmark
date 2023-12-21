
def composite_nums_between_indices(my_list):
    # Create an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a composite number
    for i in range(37, 52):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of composite numbers between indices 37 and 51
    return composite_nums
