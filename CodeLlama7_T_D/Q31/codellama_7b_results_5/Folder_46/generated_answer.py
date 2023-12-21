
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 453 elements
    if len(my_list) < 453:
        return False

    # Calculate the sum of the divisors of the number at index 453
    perfect_num = my_list[453]
    sum_divisors = 0

    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_divisors += i

    # Check if the calculated sum of divisors is equal to the number at index 453
    if sum_divisors == perfect_num:
        return True

    else:

        return False
