
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the list of integers and check if each integer is not divisible by -34
    for i in my_list:
        if i % -34 != 0:
            result.append(i)

    # Return the list of all integers not divisible by -34 from index 50 to index 200, both exclusive
    return result
