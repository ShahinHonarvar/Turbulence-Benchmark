
def if_perfect_num(my_list):
    # Check if the list has at least 321 elements
    if len(my_list) < 321:
        return False

    # Calculate the sum of the factors of the number at index 321
    sum_of_factors = 0

    for i in range(1, int(math.sqrt(my_list[321])) + 1)):
        if my_list[321] % i == 0:
            sum_of_factors += i + my_list[321] / i

    # Check if the sum of the factors is equal to the number at index 321
    if sum_of_factors == my_list[321]:
        return True

    else:

        return False
