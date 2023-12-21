
def if_perfect_num(my_list):
    # Check if the list is empty or has fewer than 41 elements
    if len(my_list) < 41:
        return False

    # Calculate the sum of the divisors of the number at index 40
    num = my_list[40]
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i + num // i

    # Return true if the number at index 40 is a perfect number
    return sum_divisors == 2 * num
