
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a prime number
    for i in range(40, 201):
        if my_list[i] == True:
            # If the element is not prime, add it to the set of composite numbers
            composite_nums.add(i)

    return composite_nums
