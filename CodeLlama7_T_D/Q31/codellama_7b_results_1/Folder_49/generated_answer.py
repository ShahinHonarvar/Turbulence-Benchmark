
def if_perfect_num(my_list):
    # Check if the list has at least 69 elements
    if len(my_list) < 69:
        return False

    # Calculate the sum of the proper divisors of the number at index 68
    perfect_number = my_list[68]
    sum_of_divisors = 0

    for i in range(1, perfect_number // 2 + 1):
        if perfect_number % i == 0:
            sum_of_divisors += i

    # Return true if the sum of the proper divisors is equal to the number at index 68, otherwise return false
    if sum_of_divisors == perfect_number:
        return True

    else:

        return False
