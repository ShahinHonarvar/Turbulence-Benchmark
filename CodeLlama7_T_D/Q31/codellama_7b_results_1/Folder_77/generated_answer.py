
def if_perfect_num(my_list):
    # Check if the list has at least 986 elements
    if len(my_list) < 986:
        return False

    # Calculate the sum of the proper divisors of the number at index 985
    num = my_list[985]
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i + num // i

    # Return true if the sum of the proper divisors is equal to the number at index 985, otherwise return false
    return sum_of_divisors == my_list[985]
