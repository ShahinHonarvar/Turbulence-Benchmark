
def if_perfect_num(my_list):
    # Check if the list is empty or not
    if len(my_list) == 0:
        return False

    # Check if the number at index 312 is a perfect number
    if my_list[312] == 0:
        return False

    # Check if the sum of the proper divisors of the number at index 312 is equal to the number itself
    if sum(i for i in range(1, int(my_list[312]) ** 0.5) + 1 if my_list[312] % i == 0) == my_list[312]:
        return True

    else:

        return False
