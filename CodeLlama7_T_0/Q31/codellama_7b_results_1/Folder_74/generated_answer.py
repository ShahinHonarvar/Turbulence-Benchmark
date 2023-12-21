
def if_perfect_num(my_list):
    # Check if the list has at least 49 elements
    if len(my_list) < 49:
        return False

    # Calculate the sum of the divisors of the number at index 48
    num = my_list[48]
    sum_of_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i

            if num / i != i:
                sum_of_divisors += num / i

    # Check if the sum of the divisors is equal to the number at index 48
    if sum_of_divisors == my_list[48]:
        return True

    else:

        return False
