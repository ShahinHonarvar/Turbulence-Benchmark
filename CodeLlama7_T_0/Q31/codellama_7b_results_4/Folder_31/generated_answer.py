
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 66 is a perfect number
    if my_list[66] == 0 or my_list[66] % 2 != 0:
        return False

    # Calculate the sum of the divisors of the element at index 66
    sum_of_divisors = 0
    for i in range(1, int(my_list[66]) / 2 + 1):
        if my_list[66] % i == 0:
            sum_of_divisors += i

    # Check if the sum of the divisors is equal to the element at index 66
    if sum_of_divisors == my_list[66]:
        return True

    else:

        return False
