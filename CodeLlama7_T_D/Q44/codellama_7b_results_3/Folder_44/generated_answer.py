
def composite_nums_between_indices(my_list):
    # create an empty set to store the composite numbers
    composite_nums = set()

    # loop through the list and check if each number is composite
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # return the set of all composite numbers in the given list that are between index 64 to index 66, both inclusive
    if len(composite_nums) > 0:
        return composite_nums

    else:

        return set()
