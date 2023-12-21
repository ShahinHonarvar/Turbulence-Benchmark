
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each element is a composite number
    for i in range(90, 201):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers between indices 90 and 200
    return composite_nums
