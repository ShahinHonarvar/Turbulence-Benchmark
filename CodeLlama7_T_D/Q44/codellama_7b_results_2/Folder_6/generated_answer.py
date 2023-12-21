
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a composite number between index 13 and index 68, both inclusive
    for i in range(len(my_list)):
        if my_list[i] > 1 and my_list[i] % 2 != 0:
            for j in range(13, 69):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 13 and index 68, both inclusive
    return composite_nums
