
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last composite numbers in the list
    start_index = None
    end_index = None
    for i in range(len(my_list)):
        if is_composite(my_list[i]):
            if start_index == None:
                start_index = i

            end_index = i

    # Return the set of all composite numbers between the indices

    return set(my_list[start_index:end_index+1])

# Check if a number is composite by dividing it by all the prime factors of it
def is_composite(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True

    return False
