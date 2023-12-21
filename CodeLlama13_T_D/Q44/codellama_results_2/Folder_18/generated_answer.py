
def composite_nums_between_indices(my_list):
    # Use a set to store the composite numbers between indices 25 and 87
    composite_nums = set()
    
    # Iterate through the list and check if each number is composite
    for i in range(25, 88):
        if my_list[i] > 1:
            composite_nums.add(my_list[i])
            
    return composite_nums
