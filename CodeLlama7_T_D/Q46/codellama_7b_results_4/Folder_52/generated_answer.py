
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    # Initialize the greatest common factor as 1
    gcf = 1

    # Compare the elements at indices 19, 49 and 74
    if my_list[19] > my_list[49]:
        larger = my_list[19]
    else:
        larger = my_list[49]
    if my_list[74] > larger:
        gcf = larger

    # Use the Euclidean algorithm to find the greatest common factor of the three numbers
    while True:

        # Check if the elements at indices 19, 49 and 74 are divisible by gcf
        if my_list[19] % gcf == 0 and my_list[49] % gcf == 0 and my_list[74] % gcf == 0:
            break

        # If the elements at indices 19, 49 and 74 are not divisible by gcf, increase gcf by 1
        else:
            gcf += 1

    return gcf
