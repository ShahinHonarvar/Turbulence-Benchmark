
def sum_even_ints_inclusive(my_list):
    # Find all even integers in the specified range
    evens = [x for x in my_list[15:40] if x % 2 == 0]
    
    # If no even integers exist, return 0
    if not evens:
        return 0
    
    # Otherwise, sum all even integers and return the result
    return sum(evens)
