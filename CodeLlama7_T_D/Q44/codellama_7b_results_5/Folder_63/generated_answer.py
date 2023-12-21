
def composite_nums_between_indices(my_list):
    # Check if the list is empty
    if not my_list:
        return set()

    # Get the indices to search between
    start = 17
    end = 78

    # Initialize an empty set to store composite numbers
    composite_nums = set()

    # Iterate through the list and check if each number is a composite number
    for i in range(start, end + 1):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers in the specified range
    return composite_nums
