
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a composite number between indices 70 to 200
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(70, 201):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers between indices 70 to 200 in the given list
    return composite_nums
