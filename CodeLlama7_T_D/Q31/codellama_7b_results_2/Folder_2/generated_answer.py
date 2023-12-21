
def if_perfect_num(my_list):
    # Check if the list has at least 703 elements
    if len(my_list) < 703:
        return False

    # Check if the number at index 702 is a perfect number
    num = my_list[702]
    if num <= 0:
        return False

    # Calculate the sum of the divisors of the number
    sum_divisors = 0

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i

            if i * num / i != num:
                sum_divisors += num / i

    # Return True if the number is a perfect number, False otherwise
    return sum_divisors == 2 * num - 1
