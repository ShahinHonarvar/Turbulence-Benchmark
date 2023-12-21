
def if_perfect_num(my_list):
    # Check if the list is empty or if it has fewer than 49 elements
    if len(my_list) < 49:
        return False

    # Calculate the sum of the divisors of the number at index 48
    perfect_number = my_list[48]
    sum_of_divisors = 0
    for i in range(1, perfect_number // 2 + 1):
        if perfect_number % i == 0:
            sum_of_divisors += i

    # Check if the sum of the divisors is equal to the number at index 48
    if sum_of_divisors == perfect_number:
        return True

    else:

        return False
