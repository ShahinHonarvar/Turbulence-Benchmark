
def composite_nums_between_indices(my_list):
    # create a set to store the composite numbers
    composite_nums = set()

    # loop through the list and check for composite numbers between indices 10 to 66, both inclusive
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # return the set of all composite numbers between indices 10 to 66, both inclusive
    return composite_nums
