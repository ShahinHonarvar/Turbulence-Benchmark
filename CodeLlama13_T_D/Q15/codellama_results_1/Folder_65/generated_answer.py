
def sum_odd_ints_inclusive(my_list):
    # Extract odd integers from index 56 to index 98, both inclusive
    odd_ints = [x for x in my_list[56:99] if x % 2 != 0]
    
    # Return the sum of odd integers
    return sum(odd_ints) or 0
