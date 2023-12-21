
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last composite numbers in the list
    first_composite = None
    last_composite = None
    for i in range(len(my_list)):
        if is_composite(my_list[i]):
            if first_composite is None:
                first_composite = i

            last_composite = i

    # Return the set of all composite numbers between the indices
    return set(my_list[first_composite:last_composite+1])

def is_composite(n):

    # Check if n is a multiple of 2 to 10
    for i in range(2, 11):
        if n % i == 0:
            return True

    # If no factors were found, n is prime
    return False
