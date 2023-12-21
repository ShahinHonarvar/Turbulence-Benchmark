
def if_perfect_num(my_list):
    # Check if the list has at least 73 elements
    if len(my_list) < 73:
        return False

    # Calculate the sum of the divisors of the number at index 72
    num = my_list[72]
    sum_of_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i + num // i

    # Check if the sum of the divisors is equal to the number at index 72
    return sum_of_divisors == num
