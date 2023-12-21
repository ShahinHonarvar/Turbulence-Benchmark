
def if_perfect_num(my_list):
    # Check if the list has at least 24 elements
    if len(my_list) < 24:
        return False

    # Calculate the sum of the proper divisors of the number at index 23
    perfect_number = my_list[23]
    sum_proper_divisors = 0
    for i in range(1, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            sum_proper_divisors += i

    # Check if the sum of the proper divisors is equal to the number at index 23
    if sum_proper_divisors == perfect_number:
        return True

    else:

        return False
