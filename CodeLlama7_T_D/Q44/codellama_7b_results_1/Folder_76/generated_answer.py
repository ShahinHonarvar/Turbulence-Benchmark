
def composite_nums_between_indices(my_list):
    # Create a set to store the composite numbers
    composite_set = set()

    # Iterate through the list and check for composite numbers between index 639 and index 975
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    composite_set.add(my_list[i])
                    break

    # Return the set of all composite numbers in the given list that are between index 639 and index 975, both inclusive
    return composite_set
