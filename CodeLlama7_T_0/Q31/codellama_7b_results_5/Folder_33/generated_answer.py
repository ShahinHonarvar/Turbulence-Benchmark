
def if_perfect_num(my_list):
    # Check if the list has at least 321 elements
    if len(my_list) < 321:
        return False

    # Calculate the sum of the proper divisors of the number at index 321
    num = my_list[321]
    sum_of_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i

            if i * num // i != num:
                sum_of_divisors += num // i

    # Check if the sum of the proper divisors is equal to the number at index 321
    if sum_of_divisors == num:
        return True

    else:

        return False
