
def if_perfect_num(my_list):
    # Check if the list has at least 97 elements
    if len(my_list) < 97:
        return False

    # Check if the number at index 96 is a perfect number
    if my_list[96] == 0 or my_list[96] % 2 != 0:
        return False

    # Calculate the sum of the divisors of the number at index 96
    sum_divisors = 1

    for i in range(2, int(my_list[96] ** 0.5) + 1):
        if my_list[96] % i == 0:
            sum_divisors += i + my_list[96] / i

    # Check if the sum of the divisors is equal to the number at index 96
    if sum_divisors == my_list[96]:
        return True

    else:

        return False
