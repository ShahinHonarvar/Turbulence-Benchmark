
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    comp_nums = set()
    
    # Iterate through the list and check if each number is composite
    for i in range(222, 223):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    comp_nums.add(my_list[i])
                    break
    
    # Return the set of composite numbers
    return comp_nums
