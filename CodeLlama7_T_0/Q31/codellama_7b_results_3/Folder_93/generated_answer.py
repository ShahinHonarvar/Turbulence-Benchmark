
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 46 elements
    if len(my_list) < 46:
        return False

    # Calculate the sum of the divisors of the number at index 45
    num = my_list[45]
    sum_of_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i

            if num / i != i:
                sum_of_divisors += num / i

    # Check if the sum of the divisors is equal to the number at index 45
    if sum_of_divisors == num:
        return True

    else:

        return False
