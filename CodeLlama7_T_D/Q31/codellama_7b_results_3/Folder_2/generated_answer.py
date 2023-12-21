
def if_perfect_num(my_list):
    # Check if the list has at least 702 elements
    if len(my_list) < 702:
        return False

    # Calculate the sum of the divisors of the number at index 702
    num = my_list[702]
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i + num // i

    # Check if the sum of the divisors is equal to the number at index 702
    return sum_of_divisors == num
