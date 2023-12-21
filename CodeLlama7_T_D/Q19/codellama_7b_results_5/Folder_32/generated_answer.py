
def all_ints_not_div_by_num(my_list):
    # create a slice of the list from index 43 to 77 (exclusive)
    slice_ = my_list[43:77]
    # initialize an empty list to store the results
    result = []

    # iterate over the slice and check if each element is not divisible by 84

    for i in slice_:
        if i % 84 != 0:
            result.append(i)

    return result
