
def if_perfect_num(my_list):
    # Check if the list has at least 34 elements
    if len(my_list) < 34:
        return False

    # Calculate the sum of the divisors of the number at index 33
    num = my_list[33]
    sum_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i

            if num / i != i:
                sum_divisors += num / i

    # Check if the sum of the divisors is equal to the number at index 33
    if sum_divisors == num:
        return True

    else:

        return False
