 def return_binary_or_hexa(my_tuple):
    # Initialize variables for sum and strings
    sum = 0
    binary_str = ""
    hexa_str = ""
    # Get indices of elements in the tuple
    a_index = my_tuple.index(my_tuple[10]) + 10
    b_index = my_tuple.index(my_tuple[12]) + 12
    # Calculate sum of integers between a and b that are not present in the tuple
    for i in range(a_index + 1, b_index):
        if my_tuple[i] not in my_tuple[a_index:b_index]:
            sum += my_tuple[i]
    # Return binary or hexadecimal representation string of the sum
    if sum % 2 == 0:
        return hexa_str
    else:
        return binary_str
