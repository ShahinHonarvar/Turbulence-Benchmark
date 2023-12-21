
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list and check if each number is composite
    for i in range(111, 111 + len(my_list)):
        if my_list[i - 111] > 1 and is_prime(my_list[i - 111])):
            composite_nums.add(my_list[i - 111])

    # Return the set of all composite numbers in the given list that are between index 111 to index 111, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
