
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 460 elements
    if len(my_list) < 460:
        return False

    # Check if the element at index 459 is a perfect number
    if my_list[459] == 1:
        return True

    # Calculate the sum of the divisors of the element at index 459
    sum_of_divisors = 0
    for i in range(2, int(my_list[459] ** 0.5) + 1):
        if my_list[459] % i == 0:
            sum_of_divisors += i + my_list[459] / i

    # Check if the sum of the divisors is equal to the element at index 459
    if sum_of_divisors == my_list[459]:
        return True

    else:

        return False
