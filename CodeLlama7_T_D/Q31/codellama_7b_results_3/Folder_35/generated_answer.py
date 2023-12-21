
def if_perfect_num(my_list):
    # Check if the list is empty or has length less than 993
    if len(my_list) < 993:
        return False

    # Calculate the sum of the divisors of the number at index 993
    num = my_list[993]
    sum_of_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i + num // i

    # Return true if the number at index 993 is a perfect number, otherwise return false
    return sum_of_divisors == 2 * num
