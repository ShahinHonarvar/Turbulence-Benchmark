
def if_perfect_num(my_list):
    # Check if the list has at least 94 elements
    if len(my_list) < 94:
        return False

    # Calculate the sum of the divisors of the number at index 93
    num = my_list[93]
    sum_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i * i != num:
                sum_divisors += num // i

    # Return true if the sum of the divisors is equal to the number at index 93, otherwise return false
    return sum_divisors == num
