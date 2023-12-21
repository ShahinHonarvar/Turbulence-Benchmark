
def find_second_largest_num(distinct_numbers):
    # Sort the list in descending order
    sorted_list = sorted(distinct_numbers, reverse=True)
    
    # Find the second largest element from index 29 to index 93, both inclusive
    for i in range(29, 94):
        if sorted_list[i] != sorted_list[i-1]:
            return sorted_list[i]
    
    # If there is no such element, return 'None'
    return None
