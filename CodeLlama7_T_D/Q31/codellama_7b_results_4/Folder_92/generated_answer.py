
def if_perfect_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return False

    # Calculate the sum of the factors of the number at index 0
    sum_of_factors = 0
    for i in range(1, my_list[0]):
        if my_list[0] % i == 0:
            sum_of_factors += i

    # Check if the sum of the factors is equal to the number at index 0
    if sum_of_factors == my_list[0]:
        return True

    else:

        return False
