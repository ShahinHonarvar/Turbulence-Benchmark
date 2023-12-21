
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers in a list
    # Assign the indices for the two numbers
    index1 = 28
    index2 = 49
    # Initialize the GCF to 1
    gcf = 1
    # Loop through the factors of both numbers
    for i in range(1, min(my_list[index1], my_list[index2]) + 1):
        if my_list[index1] % i == 0 and my_list[index2] % i == 0:
            gcf = i

    return gcf
