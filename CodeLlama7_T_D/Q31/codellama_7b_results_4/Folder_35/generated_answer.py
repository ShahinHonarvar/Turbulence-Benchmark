
def if_perfect_num(my_list):
    # Check if the list has at least 994 elements
    if len(my_list) < 994:
        return False

    # Calculate the sum of the proper divisors of the number at index 993
    num = my_list[993]
    sum_divisors = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i

            if num / i != i:
                sum_divisors += num // i

    # Return true if the number at index 993 is a perfect number, otherwise false
    return sum_divisors == 2 * num
