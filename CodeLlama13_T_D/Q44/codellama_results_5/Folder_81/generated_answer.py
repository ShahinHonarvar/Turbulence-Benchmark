
def composite_nums_between_indices(my_list):
    # Find the indices of the start and end of the specified range
    start_idx = 20
    end_idx = 200
    
    # Create a set to store the composite numbers
    composite_nums = set()
    
    # Iterate through the list and check if each number is composite
    for i in range(start_idx, end_idx+1):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]**0.5) + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break
    
    return composite_nums
