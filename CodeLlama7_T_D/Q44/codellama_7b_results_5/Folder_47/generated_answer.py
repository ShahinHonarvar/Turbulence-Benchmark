
def composite_nums_between_indices(my_list):
    # Create an empty set to store the composite numbers
    composite_nums = set()
    # Loop through the list and check if each element is composite between indices 75 and 88
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(75, 89):
                if i == j and my_list[i] % 2 != 0:
                    composite_nums.add(my_list[i])
    # Return the set of all composite numbers between indices 75 and 88
    return composite_nums
