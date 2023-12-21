
def if_perfect_num(my_list):
    # Check if the list has at least 98 elements
    if len(my_list) < 98:
        return False

    # Calculate the sum of the proper divisors of the number at index 97
    sum_of_divisors = 1
    for i in range(2, int(my_list[97] ** 0.5) + 1):
        if my_list[97] % i == 0:
            sum_of_divisors += i + my_list[97] // i
    # Check if the sum of the proper divisors is equal to the number at index 97
    return sum_of_divisors == my_list[97]
