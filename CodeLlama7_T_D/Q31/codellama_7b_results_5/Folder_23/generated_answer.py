
def if_perfect_num(my_list):
    # Check if the list has at least 70 elements
    if len(my_list) < 70:
        return False

    # Get the value of the 69th element in the list
    num = my_list[69]

    # Calculate the sum of the divisors of the number
    sum_of_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i * num > num:
                break

    # Check if the sum of the divisors is equal to the number itself
    return sum_of_divisors == num
