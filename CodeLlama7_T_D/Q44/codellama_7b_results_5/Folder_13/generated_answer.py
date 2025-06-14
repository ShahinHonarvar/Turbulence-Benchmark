
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each element is a composite number between indices 21 to 97, both inclusive
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(21, 98):
                if my_list[i] % j == 0 and i >= 21 and i <= 97:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers between indices 21 to 97, both inclusive
    return composite_nums
