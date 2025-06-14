
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each element is a composite number
    for i in range(5, 8):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i])**0.5 + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 5 and index 7, inclusive
    return composite_nums
