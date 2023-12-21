
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 247 is a perfect number
    if my_list[247] == 0:
        return False

    # Check if the sum of the divisors of the element at index 247 is equal to the element itself
    sum_divisors = 1
    for i in range(2, int(my_list[247] ** 0.5) + 1):
        if my_list[247] % i == 0:
            sum_divisors += i + my_list[247] / i
    if sum_divisors == my_list[247]:
        return True

    # If none of the above conditions are met, return false
    else:
        return False
