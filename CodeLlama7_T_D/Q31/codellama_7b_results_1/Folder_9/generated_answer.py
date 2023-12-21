
def if_perfect_num(my_list):
    # Check if the list has at least 25 elements
    if len(my_list) < 25:
        return False

    # Calculate the sum of the divisors of the number at index 24
    num = my_list[24]
    sum_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i

            if num / i != i:
                sum_divisors += num / i

    # Check if the sum of the divisors is equal to the number at index 24
    return sum_divisors == my_list[24]
